module Intensity
  class Shooter
    include Enumerable

    attr_reader :increments, :state

    def initialize start, waypoint, steps = 10
      @state = start
      @steps = steps
      @counter = 0
      @increments = Shooter.diff(start, waypoint).map { |d| d / @steps.to_f }
    end

    def done
      @counter == @steps * 2
    end

    def move
      3.times do |i|
        @state[i] += @increments[i]
      end
      @counter += 1
    end

    def each
      until done
        move
        yield self
      end
    end

    def Shooter.diff start, waypoint
      diff = []
      3.times do |i|
        diff.push waypoint[i] - start[i]
      end
      diff
    end

    def Shooter.starting_point
      s = []
      3.times do
        x = Random.rand(3) + 3
        x = 0 - x if Random.rand(2) == 1
        s.push x
      end
      s
    end

    def Shooter.waypoint
      [0, 0, 0]
    end

    def Shooter.step_value
      Random.rand(8) + 32
    end

    def Shooter.colour
      c = []
      3.times do
        c.push Random.rand(127)
      end
      c[Random.rand(2)] += Random.rand(192)
      c
    end
  end
end
