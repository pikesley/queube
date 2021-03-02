require_relative 'intensity'
require_relative 'shooter'
require_relative 'sphere'
require 'json'
require 'redis'

@redis = Redis.new(url: "redis://#{ENV['REDIS']}")
@cube = Intensity::Cube.new
@terminate = false

Signal.trap('TERM') do
  puts "Caught signal `TERM`"
  @terminate = true
end

loop do
  @shooter = Intensity::Shooter.new Intensity::Shooter.starting_point, Intensity::Shooter.waypoint, Intensity::Shooter.step_value
  @colour = Intensity::Shooter.colour

  @shooter.each do |s|
    @cube.illuminate_location s.state, @colour
    @redis.rpush "lights", {data: @cube}.to_json
    sleep 0.05
  end

  @redis.rpush "lights", {data: "EOF"}.to_json

  if @terminate
    break
  end
end

sleep 1
@redis.flushall
