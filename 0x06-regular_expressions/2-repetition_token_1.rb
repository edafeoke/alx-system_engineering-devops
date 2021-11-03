#!/usr/bin/env ruby

def reg(arg)
  puts arg.scan(/hb?tn/).join
end

reg ARGV[0]
