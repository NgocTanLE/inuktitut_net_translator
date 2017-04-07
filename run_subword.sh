
lang="en"
input_file="in_en_data/text_all.$lang"
codes_file="subword_segmentation/codes_file"
test_file="in_en_data/text_all.$lang"
out_dir="subword_segmentation/$1/segmented_file.$lang"
touch $codes_file
mkdir "subword_segmentation/$1"
./subword-nmt/learn_bpe.py -s $1 < $input_file > $codes_file
./subword-nmt/apply_bpe.py -c $codes_file < $test_file > $out_dir
