require_relative '../shooter'

module Intensity
  describe Shooter do
    context 'increments' do
      it 'solves an easy case' do
        s = described_class.new [-2, -2, -2], [0, 0, 0], 2
        expect(s.increments).to eq [1, 1, 1]
      end

      it 'solves a trickier case' do
        s = described_class.new [3, -3, 3], [0, 0, 0], 3
        expect(s.increments).to eq [-1, 1, -1]
      end

      it 'solves a case with fractions' do
        s = described_class.new [-1.5, 2.4, -0.5], [1, 1, 0.3], 4
        expect(s.increments).to eq [0.625, -0.35, 0.2]
      end
    end

    it 'finds the diffs' do
      expect(described_class.diff [-1, -1, -1], [0, 0, 0]).to eq [1, 1, 1]
      expect(described_class.diff [-2, 2, -3], [0, 0, 0]).to eq [2, -2, 3]
    end

    context 'move' do
      it 'moves' do
        s = described_class.new [-1, -1, -1], [0, 0, 0], 1
        expect(s.state).to eq [-1, -1, -1]
        s.move
        expect(s.state).to eq [0, 0, 0]
        s.move()
        expect(s.state).to eq [1, 1, 1]
      end

      it 'knows when it has no more moves' do
        s = described_class.new [-1, -1, -1], [0, 0, 0], 1
        s.move
        expect(s.done).to be false
        s.move
        expect(s.done).to be true
      end
    end

    context 'iterator' do
      it 'has an iterator' do
        s = described_class.new [-1, -1, -1], [0, 0, 0], 4
        count = 0
        s.each do |state|
          count += 1
        end
        expect(s.state).to eq [1, 1, 1]
        expect(count).to eq 8
      end
    end

    context 'starting points' do
      it 'generates valid starting points' do
        expect(Shooter.starting_point.map { |h| h.abs}.all? { |i| i > 1}).to be true
      end

      it 'generates valid waypoints' do
        expect(Shooter.waypoint).to eq [0, 0, 0]
      end

      it 'generates step values' do
        expect(Shooter.step_value).to be_between 8, 40
      end
    end

    it 'generates random colours'
  end
end
