output printname {
  value = "Hello ${var.username} age is ${var.age}"

}

output printlame {
  value = "Hello ${var.users[0]} age is ${var.age}"

}