apt-get update
apt-get install -y apache2
apt-get install -y php5 php5-gd
apt-get install -y vim
apt-get install -y curl

cp /vagrant/vagrant-provision/etc/apache2/sites-available/default /etc/apache2/sites-available
service apache2 restart
