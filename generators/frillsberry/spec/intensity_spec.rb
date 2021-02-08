describe Intensity do
  context 'intensity by distance' do
    {
      # 0 => 1,
      # 1 => 0.5,
      # 2 => 0.125,
      # 3 => 0.05555555555555555,
      # 4 => 0.03125
      0 => 1,
      1 => 1,
      2 => 1
    }.each_pair do |distance, intensity|
      it "has intensity #{intensity} at distance #{distance}" do
        expect(Intensity.intensity distance).to eq intensity
      end
    end
  end

  context 'distance to neighbours' do
    {
      [[0, 0, 0], [0, 0, 1]] => 1.0,
      [[0, 0, 0], [0, 1, 1]] => Math.sqrt(2),
      [[-1, 0, -1], [0, 1, 0]] => Math.sqrt(3),
      [[0, 0, 0], [0, 0, -1]] => 1.0,
      [[-1, -1, -1], [1, 1, 0]] => 3.0,
      [[-1, -1, 1], [1, 1, -1]] => Math.sqrt(3) * 2,
      [[0, 0, 0], [0, 0, 0]] => 0
    }.each_pair do |coords, distance|
      it "knows the distance from #{coords[0]} to #{coords[1]} is #{distance}" do
        expect(Intensity.distance coords[0], coords[1]).to eq distance
      end
    end

    context 'fractional distances' do
      {
        [[0, 0, 0], [0.5, 0, 0]] => 0.5,
        [[0.5, 0.5, 0.5], [0, 0, 0]] => Math.sqrt(3) / 2
      } .each_pair do |coords, distance|
        it "knows the distance from #{coords[0]} to #{coords[1]} is #{distance}" do
          expect(Intensity.distance coords[0], coords[1]).to eq distance
        end
      end
    end

    context 'scale colours' do
      it 'scales a colour by 0.5' do
        expect(Intensity.scale_colour [255, 127, 0], 0.5).to eq [128, 64, 0]
      end
    end

    context 'gamma-correct colours' do
      it 'gamma-corrects a colour' do
        expect(Intensity.gamma_corrected [250, 129, 0]).to eq [241, 38, 0]
      end
    end
  end
end
