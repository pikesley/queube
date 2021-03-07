require_relative 'intensity'
require_relative 'shooter'
require_relative 'sphere'
require 'json'
require 'redis'

@redis = Redis.new(url: "redis://#{ENV['REDIS']}")
@terminate = false

Signal.trap('TERM') do
  puts "Caught signal `TERM`"
  @terminate = true
end

loop do
  if @redis.llen("queube").to_i < 2 then
    @shooter = Intensity::Shooter.new Intensity::Shooter.starting_point, Intensity::Shooter.waypoint, Intensity::Shooter.step_value
    @colour = Intensity::Shooter.colour

    @payload = {
      colour: @colour,
      states: []
    }

    @shooter.each do |s|
      @payload[:states].append Intensity::Cube.new
      @payload[:states].last.illuminate_location s.state, @colour
    end
    @redis.rpush "queube", @payload.to_json

  else
    sleep 1
  end

  if @terminate
    break
  end
end

# sleep 1
# @redis.flushall
