require_relative 'intensity'
require_relative 'shooter'
require_relative 'sphere'
require 'json'

@cube = Intensity::Cube.new

require 'bunny'
connection = Bunny.new hostname: "#{ENV['RABBIT']}:5672", username: 'pi', password: 'raspberry'
  connection.start
channel = connection.create_channel
queue = channel.queue('queube')

loop do
  @shooter = Intensity::Shooter.new Intensity::Shooter.starting_point, Intensity::Shooter.waypoint, Intensity::Shooter.step_value
  @colour = Intensity::Shooter.colour

  @shooter.each do |s|
    @cube.illuminate_location s.state, @colour
    channel.default_exchange.publish({data: @cube}.to_json, routing_key: queue.name)
    sleep 0.05
  end
end
