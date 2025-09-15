CREATE DATABASE IF NOT EXISTS `DDOS_Attack` CHARACTER SET latin1;


USE `DDOS_Attack`;


/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `s.no` int(100) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`s.no`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `intursion` */

insert  into `user`(`s.no`,`name`,`email`,`password`,`phone`) values (1,'Adi','adi@gmail.com','123','9966885599');

