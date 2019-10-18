#!/usr/bin/env bash

cat << EOF > f.yaml
#BANNER
#Banner file location.
banner:
  location: classpath:banner.txt
  charset: UTF-8

spring:
  pool:
    corePoolSize: 20
    maxPoolSize: 100
    keepAliveSeconds: 300
    queueCapacity: 500
  main:
    banner-mode: console
    #off
  mvc:
    throw-exception-if-no-handler-found: true
  aop:
    auto: true
    proxy-target-class: false
  resources:
    add-mappings: false

  devtools:
    restart:
    #热部署生效
      enabled: true
#      enabled: false
    #设置重启的目录
      additional-paths: src/main/java
    #classpath目录下的resources文件夹内容修改不重启
#      exclude: resources/**
      trigger-file: classpath:trigger.txt
  http:
    encoding:
      charset: UTF-8
 # 数据库访问配置
  datasource:
    url: jdbc:mysql://$A_HOST:$A_PORT/baas_platform?allowMultiQueries=true&serverTimezone=UTC&useSSL=false&useUnicode=true&characterEncoding=UTF-8
    username: root
    password: Zsba@mysql2018*
    driver-class-name: com.mysql.jdbc.Driver
#    platform: mysql
 # 使用druid
    type: com.alibaba.druid.pool.DruidDataSource
    druid:
      maxActive: 20
      initialSize: 1
      maxWait: 60000
      minIdle: 1
      timeBetweenEvictionRunsMillis: 60000
      minEvictableIdleTimeMillis: 300000
      validationQuery: SELECT 1 FROM DUAL
      testWhileIdle: true
      testOnBorrow: false
      testOnReturn: false
      poolPreparedStatements: true
      maxOpenPreparedStatements: 20

mybatis:
  config-location: classpath:config/mybatis/mybatis-config.xml
  mapperLocations: classpath:config/mybatis/mapper/**/*Mapper.xml
  typeAliasesPackage: com.zsbatech.**.model
  checkConfigLocation: true

# tomcat最大线程数，默认为200
server:
  tomcat:
    max-threads:  800
    # tomcat的URI编码
    uri-encoding: UTF-8
  port: 8495
  ssl:
    key-store: classpath:config/keystore/keystore.p12
    key-store-password: uniapp
    key-store-type: PKCS12

logging:
  config: classpath:config/log/log4j2.xml
#  level:
#    org.springframework:  WARN

unipassport:
  url: http://api.unipassport.dev.tusdao.com

agent:
  port: 8017
  height:
    url: http://api.baas-cluster.dev.tusdao.com/cluster/BlockInfo/BlockInfo?sign=test
EOF
