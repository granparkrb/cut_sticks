#!/usr/bin/env ruby

require 'pry'

sticks = ARGV[0] ? ARGV[0].split(",").map(&:to_i) : [76,594,17,6984,26,57,9,876,5816,73,969,527,49]
max_cut_times = ARGV[1] ? ARGV[1].to_i : 789
rank = ARGV[2] ? ARGV[2].to_i : 459

puts sticks.inspect
puts max_cut_times
puts rank

def answer(len)
  puts "answer: #{len}"
  exit 0
end

if rank == 1
  answer(sticks.max)
end

len = 0.0
thresh = 0
current_sticks = sticks
binding.pry

while (true) do
  while (true) do
    len = current_sticks.inject {|sum, n| sum += n } / rank.to_f
    thresh = len.floor
    new_sticks = current_sticks.select {|n| n >= thresh }
    break if new_sticks.size == current_sticks.size
    current_sticks = new_sticks
  end
  puts "current length: #{len}"

  new_sticks = current_sticks.select {|n| n >= thresh * 2}
  break if new_sticks.size == current_sticks.size
  rank -= (current_sticks - new_sticks).size
  puts "rank: #{rank}"
  puts "new_sticks: #{new_sticks.inspect}"
  current_sticks = new_sticks
end

current_sticks.sort!.reverse!

total_num = current_sticks.size
cut_times = 0
binding.pry
while (true) do
  next_len = 0.0
  current_sticks.each do |stick|
    increment = (stick / len).floor - 1
    total_num += increment
    cut_times += increment
    if cut_times > max_cut_times
      puts "giving up"
      exit -1
    end
    next_len_cand =  stick / (increment + 2).to_f
    next_len = next_len_cand if next_len_cand > next_len
  end
  binding.pry
  break if total_num >= rank
  len = next_len
end

puts "sticks: #{current_sticks.inspect}"
answer(len)
