provider "aws" {
    region = "us-east-1"
}
resource "aws_vpc" "tf_vpc" {
    cidr_block = "10.0.0.0/16"
    instance_tenancy = "default"  


}
resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.tf_vpc.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "Main"
  }
}
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.tf_vpc.id

  tags = {
    Name = "main"
  }
}
resource "aws_security_group" "allow_tls" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_vpc.tf_vpc.id

  ingress {
    description      = "TLS from VPC"
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
    cidr_blocks      = [aws_vpc.tf_vpc.cidr_block]
    # ipv6_cidr_blocks = [aws_vpc.tf_vpc.ipv6_cidr_block]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_tls"
  }
}

resource "aws_network_interface" "my_interface" {
  subnet_id       = aws_subnet.main.id
  private_ips     = ["10.0.1.50"]
  security_groups = [aws_security_group.allow_tls.id]#TODO

#   attachment {
#     instance     = aws_instance.test.id
#     device_index = 1
#   }
}




resource "aws_instance" "main_instance" {
  ami           = "ami-0dfcb1ef8550277af" # us-west-2
  instance_type = "t2.micro"

  network_interface {
    network_interface_id = aws_network_interface.my_interface.id
    device_index         = 0
  }
}
resource "aws_eip" "lb" {
  instance = aws_instance.main_instance.id
  vpc      = true
}



#   credit_specification {
#     cpu_credits = "unlimited"
#   }
