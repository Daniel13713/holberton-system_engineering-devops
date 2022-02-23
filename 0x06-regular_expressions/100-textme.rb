#!/usr/bin/env ruby
sen=ARGV[0].scan(/\[from:([\w\+]+)\]/).join
rec=ARGV[0].scan(/\[to:([\w\+]+)\]/).join
fla=ARGV[0].scan(/\[flags:([\W\d]+)\]/).join
puts [sen, rec, fla].join(',')

