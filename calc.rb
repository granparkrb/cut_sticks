#!/usr/bin/env ruby

#require 'pry'

sticks = [ 76,594,17,6984,26,57,9,876,5816,73,969,527,49 ]
max_cut_times = 789
rank = 459

answer = sticks.max
cur_sticks = sticks

y = 0
while (y < max_cut_times) do

  x = 0
  while (x < max_cut_times) do
    answer = cur_sticks.inject {|sum, n| sum + n} / rank.to_f
    puts answer
    new_sticks = cur_sticks.select {|n| n > answer}
    #puts new_sticks.inspect
    break if new_sticks.size == cur_sticks.size
    cur_sticks = new_sticks
  end

  puts "answer?: #{answer}"

  #binding.pry
  new_sticks = cur_sticks.select {|n| n >= answer * 2}
  break if new_sticks.size == cur_sticks.size
  rank -= (cur_sticks - new_sticks).size
  puts "rank: #{rank}"
  puts "new_sticks: #{new_sticks.inspect}"
  cur_sticks = new_sticks
end

puts answer
