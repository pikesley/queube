module Intensity
  describe Cube do
    let(:subject) { described_class.new }

    it 'is an array of arrays of arrays' do
      expect(subject).to eq [
[
[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
],
[
[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
],
[
[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
]
]
    end

    context 'set values' do
      it 'allows us to set the centre value' do
        subject.set 0, 0, 0, [0, 255, 0]
        expect(subject).to eq [
      		[
      			[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
      			[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
      			[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
      		],
      		[
      			[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
      			[[0, 0, 0], [0, 255, 0], [0, 0, 0]],
      			[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
      		],
      		[
      			[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
      			[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
      			[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
      		]
      	]
      end
    end

    it 'allows us to set a different value' do
      subject.set 0, 1, 1, [255, 0, 0]
      expect(subject).to eq [
    		[
    			[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    			[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    			[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    		],
    		[
    			[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    			[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    			[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    		],
    		[
    			[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    			[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    			[[0, 0, 0], [255, 0, 0], [0, 0, 0]]
    		]
    	]
    end
  end
end