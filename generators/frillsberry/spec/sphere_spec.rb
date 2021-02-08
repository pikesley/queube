require_relative '../sphere' 

module Cube::Bit
  describe Sphere do 
    [
      {
         centre: [0, 0, 0],
         radius: 1,
         points: [
           [-1, 0, 0], [0, -1, 0], [0, 0, -1],
           [0, 0, 0],
           [0, 0, 1], [0, 1, 0], [1, 0, 0]
         ]
      },
      {
        centre: [0.5, 0, 1],
        radius: 0.5,
        points: [
          [0, 0, 1], [1, 0, 1]
        ]
      },
      {
        centre: [0.5, 0.5, 0.5],
        radius: Math.sqrt(3) / 2,
        points: [
          [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
          [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]
        ]
      },
      {
        centre: [0, 0, 0],
        radius: Math.sqrt(2),
        points: [
          [-1, -1, 0], [-1, 0, -1], [-1, 0, 0],
          [-1, 0, 1], [-1, 1, 0], [0, -1, -1],
          [0, -1, 0], [0, -1, 1], [0, 0, -1],
          [0, 0, 0],
          [0, 0, 1], [0, 1, -1], [0, 1, 0],
          [0, 1, 1], [1, -1, 0], [1, 0, -1],
          [1, 0, 0], [1, 0, 1], [1, 1, 0]
        ]
      },
      {
        centre: [0.1, 0.1, 0.1],
        radius: 0.2,
        points: [
          [0, 0, 0]
        ]
      }
    ].each do |data|
      it "contains the correct %d points for a %.3f-radius sphere at %s" % [
        data[:points].count, data[:radius], data[:centre]
      ] do
        s = described_class.new data[:centre], data[:radius]
        expect(s.points).to match_array data[:points]
      end
    end
  end
end
