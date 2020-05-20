Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"

  # VM Options
  config.vm.provider "virtualbox" do |v|
    v.memory = 3000
    v.cpus = 2
  end

  # Port Forwarding
  config.vm.network :forwarded_port, guest: 80, host: 9000

  # Install dev tools
  config.vm.provision "shell", inline: "sudo apt-get -qy update"
  config.vm.provision "shell", inline: "sudo apt-get -qy install python3-pip"
  config.vm.provision "shell", inline: "python3 -m pip install redis"
  config.vm.provision "shell", inline: "python3 -m pip install flask"

  # Start docker containers
  config.vm.provision "docker" do |d|
    d.run "redis", image: "redis", args: "-p 6379:6379"
  end

end
