module Cube
  module Bit
    class Sphere 
      attr_reader :points

      def initialize centre, radius 
        @centre = centre
        @radius = radius
        @points = []
        (-1..1).each do |x|
          (-1..1).each do |y|
            (-1..1).each do |z|
              position = [x, y, z]
              @points.push position if Intensity.distance(@centre, position) <= @radius
            end
          end
        end
      end
    end
  end
end
