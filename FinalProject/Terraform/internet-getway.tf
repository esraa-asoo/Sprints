data "aws_vpc" "main" {
  id = " vpc-00d3ce48b1a84ed56 "
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
}