# Question 01
- P2P connection.
- file of size 'S' Mb
- From server to 'N' peers
- Each peer sends data of 'M' Mb chunk
- Server's upload speed is 's' Mb
- Each peer has upload speed of 'u' Mb
- and 'd' Download speed
- Assume there are no processing delay and no protocol overheads
- The peers download the chunks using Rarest-First mechanism
- Compute the minimum distribution time by showing actual chunks distributed at
  each state of distribution
- For simplicity of computation, you can assume that 'd' is an integer multiple
  of 'u' and 's' is an integer multiple of 'M'
- ./program -S < file size in Mbits > -N < num of peers > -M < chunk size in
  Mbits > -s < server upload speed in Mbps > -u < peer upload speed in Mbps > -d
  < peer download speen in Mbps >