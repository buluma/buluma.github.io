---
title: Digitalocean Sizes and Images
---

# Digitalocean Sizes and Images

I tend to forget the output of `doctl compute size list -t ${DIGITALOCEAN_TOKEN}` and `doctl compute image list -t ${DIGITALOCEAN_TOKEN} --public`, so here is a dump if the two commands.

## Sizes.

|slug|memory (mb)|vcpu|disk (gb)|price/month($)|price/hour($)|
|----|------|----|----|---------------|--------------|
|s-1vcpu-1gb|1024|1|25|5.00|0.007440|
|512mb|512|1|20|5.00|0.007440|
|s-1vcpu-2gb|2048|1|50|10.00|0.014880|
|1gb|1024|1|30|10.00|0.014880|
|s-3vcpu-1gb|1024|3|60|15.00|0.022320|
|s-2vcpu-2gb|2048|2|60|15.00|0.022320|
|s-1vcpu-3gb|3072|1|60|15.00|0.022320|
|s-2vcpu-4gb|4096|2|80|20.00|0.029760|
|2gb|2048|2|40|20.00|0.029760|
|s-4vcpu-8gb|8192|4|160|40.00|0.059520|
|m-1vcpu-8gb|8192|1|40|40.00|0.059520|
|c-2|4096|2|25|40.00|0.059520|
|4gb|4096|2|60|40.00|0.059520|
|c2-2vcpu-4gb|4096|2|50|45.00|0.066960|
|g-2vcpu-8gb|8192|2|25|60.00|0.089290|
|gd-2vcpu-8gb|8192|2|50|65.00|0.096730|
|m-16gb|16384|2|60|75.00|0.111610|
|s-8vcpu-16gb|16384|8|320|80.00|0.119050|
|m-2vcpu-16gb|16384|2|50|80.00|0.119050|
|s-6vcpu-16gb|16384|6|320|80.00|0.119050|
|c-4|8192|4|50|80.00|0.119050|
|8gb|8192|4|80|80.00|0.119050|
|c2-4vpcu-8gb|8192|4|100|90.00|0.133930|
|m3-2vcpu-16gb|16384|2|150|100.00|0.148810|
|g-4vcpu-16gb|16384|4|50|120.00|0.178570|
|so-2vcpu-16gb|16384|2|300|125.00|0.186010|
|m6-2vcpu-16gb|16384|2|300|125.00|0.186010|
|gd-4vcpu-16gb|16384|4|100|130.00|0.193450|
|m-32gb|32768|4|90|150.00|0.223210|
|so1_5-2vcpu-16gb|16384|2|450|155.00|0.230650|
|m-4vcpu-32gb|32768|4|100|160.00|0.238100|
|s-8vcpu-32gb|32768|8|640|160.00|0.238100|
|c-8|16384|8|100|160.00|0.238100|
|16gb|16384|8|160|160.00|0.238100|
|c2-8vpcu-16gb|16384|8|200|180.00|0.267860|
|m3-4vcpu-32gb|32768|4|300|195.00|0.290180|
|g-8vcpu-32gb|32768|8|100|240.00|0.357140|
|s-12vcpu-48gb|49152|12|960|240.00|0.357140|
|so-4vcpu-32gb|32768|4|600|250.00|0.372020|
|m6-4vcpu-32gb|32768|4|600|250.00|0.372020|
|gd-8vcpu-32gb|32768|8|200|260.00|0.386900|
|m-64gb|65536|8|200|300.00|0.446430|
|so1_5-4vcpu-32gb|32768|4|900|310.00|0.461310|
|m-8vcpu-64gb|65536|8|200|320.00|0.476190|
|s-16vcpu-64gb|65536|16|1280|320.00|0.476190|
|c-16|32768|16|200|320.00|0.476190|
|32gb|32768|12|320|320.00|0.476190|
|c2-16vcpu-32gb|32768|16|400|360.00|0.535710|
|m3-8vcpu-64gb|65536|8|600|390.00|0.580360|
|g-16vcpu-64gb|65536|16|200|480.00|0.714290|
|s-20vcpu-96gb|98304|20|1920|480.00|0.714290|
|48gb|49152|16|480|480.00|0.714290|
|so-8vcpu-64gb|65536|8|1200|500.00|0.744050|
|m6-8vcpu-64gb|65536|8|1200|500.00|0.744050|
|gd-16vcpu-64gb|65536|16|400|520.00|0.773810|
|m-128gb|131072|16|340|600.00|0.892860|
|so1_5-8vcpu-64gb|65536|8|1800|620.00|0.922620|
|m-16vcpu-128gb|131072|16|400|640.00|0.952380|
|s-24vcpu-128gb|131072|24|2560|640.00|0.952380|
|c-32|65536|32|400|640.00|0.952380|
|64gb|65536|20|640|640.00|0.952380|
|c2-32vpcu-64gb|65536|32|800|720.00|1.071430|
|m3-16vcpu-128gb|131072|16|1200|785.00|1.168150|
|m-24vcpu-192gb|196608|24|600|960.00|1.428570|
|g-32vcpu-128gb|131072|32|400|960.00|1.428570|
|s-32vcpu-192gb|196608|32|3840|960.00|1.428570|
|so-16vcpu-128gb|131072|16|2400|1000.00|1.488100|
|m6-16vcpu-128gb|131072|16|2400|1000.00|1.488100|
|gd-32vcpu-128gb|131072|32|800|1040.00|1.547620|
|m-224gb|229376|32|500|1100.00|1.636900|
|m3-24vcpu-192gb|196608|24|1800|1175.00|1.748510|
|g-40vcpu-160gb|163840|40|500|1200.00|1.785710|
|so1_5-16vcpu-128gb|131072|16|3600|1240.00|1.845240|
|m-32vcpu-256gb|262144|32|800|1280.00|1.904760|
|gd-40vcpu-160gb|163840|40|1000|1300.00|1.934520|
|so-24vcpu-192gb|196608|24|3600|1500.00|2.232140|
|m6-24vcpu-192gb|196608|24|3600|1500.00|2.232140|
|m3-32vcpu-256gb|262144|32|2400|1565.00|2.328870|
|so1_5-24vcpu-192gb|196608|24|5400|1850.00|2.752980|
|so-32vcpu-256gb|262144|32|4800|2000.00|2.976190|
|m6-32vcpu-256gb|262144|32|4800|2000.00|2.976190|
|so1_5-32vcpu-256gb|262144|32|7200|2480.00|3.690480|

## images

|slug|distribution|disk (gb)|name|
|----|------------|---------|----|
|centos-6-x32|CentOS|20|6.9 x32|
|centos-6-x64|CentOS|20|6.9 x64|
|ubuntu-16-04-x32|Ubuntu|20|16.04.6 (LTS) x32|
|freebsd-12-x64|FreeBSD|20|12.1 ufs x64|
|rancheros|RancherOS|20|v1.5.6|
|centos-8-x64|CentOS|15|8.2 x64|
|debian-10-x64|Debian|15|10 x64|
|debian-9-x64|Debian|15|9 x64|
|freebsd-11-x64-zfs|FreeBSD|15|11.4 zfs x64|
|freebsd-11-x64-ufs|FreeBSD|15|11.4 ufs x64|
|centos-7-x64|CentOS|20|7.6 x64|
|fedora-32-x64|Fedora|15|32 x64|
|ubuntu-18-04-x64|Ubuntu|15|18.04 (LTS) x64|
|ubuntu-20-04-x64|Ubuntu|15|20.04 (LTS) x64|
|ubuntu-16-04-x64|Ubuntu|15|16.04 (LTS) x64|
|ubuntu-20-10-x64|Ubuntu|15|20.10 x64|
|fedora-33-x64|Fedora|15|33 x64|
|freebsd-12-x64-ufs|FreeBSD|20|12.2 ufs x64|
|freebsd-12-x64-zfs|FreeBSD|15|12.2 zfs x64|
|freebsd-12-1-x64-ufs|FreeBSD|20|12.1 ufs x64|
|freebsd-12-1-x64-zfs|FreeBSD|20|12.1 zfs x64|
|skaffolder-18-04|Ubuntu|25|Skaffolder 3.0 on Ubuntu 18.04|
|izenda-18-04|Ubuntu|20|Izenda 3.3.1 on Ubuntu 18.04|
|quickcorp-qcobjects-18-04|Ubuntu|25|QCObjects 2.1.157 on Ubuntu 18.04|
|fathom-18-04|Ubuntu|25|Fathom on 18.04|
|optimajet-workflowserver-18-04|Ubuntu|25|WorkflowServer 2.5 on Ubuntu 18.04|
|nimbella-18-04|Ubuntu|25|Nimbella Lite on Ubuntu 18.04|
|snapt-snaptaria-18-04|Ubuntu|25|Snapt Aria 2.0.0 on Ubuntu 18.04|
|snapt-snaptnova-18-04|Ubuntu|25|Snapt Nova ADC (Load Balancer, WAF) 1.0.0 on Ubuntu 18.04|
|weconexpbx-7-6|CentOS|25|WeconexPBX 2.4-1 on CentOS 7.6|
|bitwarden-18-04|Ubuntu|50|Bitwarden 1.32.0 on Ubuntu 18.04|
|buddy-18-04|Ubuntu|160|Buddy on Ubuntu 18.04|
|sharklabs-minecraftjavaedi-18-04|Ubuntu|25|Minecraft: Java Edition Server 1.0 on Ubuntu 18.04|
|selenoid-18-04|Ubuntu|25|Selenoid 1.10.0 on Ubuntu 18.04|
|litespeedtechnol-openlitespeednod-18-04|Ubuntu|25|OpenLiteSpeed NodeJS 12.16.3 on Ubuntu 20.04|
|simontelephonics-freepbx-7-6|CentOS|25|FreePBX® 15 on CentOS 7.6|
|buddy-repman-18-04|Ubuntu|25|Repman 0.4.1 on Ubuntu 18.04 (LTS)|
|strapi-18-04|Ubuntu|50|Strapi 3.1.0 on Ubuntu 18.04|
|wftutorials-purdm-18-04|Ubuntu|25|Purdm 0.3a on Ubuntu 18.04|
|caprover-18-04|Ubuntu|25|CapRover 1.8.0 on Ubuntu 18.04|
|searchblox-searchbloxenterp-7-6|CentOS|320|SearchBlox Enterprise Search 9.2.1 on CentOS 7.6|
|gitea-18-04|Ubuntu|25|Gitea 1.12.4 on Ubuntu 20.04|
|kandralabs-zulip-18-04|Ubuntu|50|Zulip 3.2 on Ubuntu 18.04|
|vodianetworks-vodiaphonesystem-10|Debian|25|Vodia Multi-tenant Cloud PBX 66 on Debian 10 x64|
|flipstarter-18-04|Ubuntu|25|Flipstarter 1.1.1 on Ubuntu 18.04|
|gluu-gluuserverce-18-04-3|Ubuntu|160|Gluu Server CE 4.2.1 on Ubuntu 20.04 (LTS)|
|netfoundry-7-6|CentOS|25|NetFoundry Zero Trust Networking 7.3.0 on CentOS 7.8|
|aplitel-vitalpbx-7|CentOS|25|VitalPBX 3.0.4-1 on Centos 7.8|
|cloudron-18-04|Ubuntu|25|Cloudron 5.6.3 on Ubuntu 18.04|
|sharklabs-pacvim-18-04|Ubuntu|25|PacVim on Ubuntu 18.04|
|eltrino-magento2opensour-18-04|Ubuntu|80|Magento 2 Open Source 1.3.1 on Ubuntu 20.04 (LTS)|
|solidinvoice-18-04|Ubuntu|25|SolidInvoice 2.0.3 on Ubuntu 18.04|
|opencart-18-04|Ubuntu|25|OpenCart 3.0.3 on Ubuntu 18.04|
|unlight-openunlight-18-04|Ubuntu|30|Open Unlight 1.0.0.pre1 on Ubuntu 18.04|
|supabase-supabaserealtime-18-04|Ubuntu|20|Supabase Realtime 0.7.5 on Ubuntu 18.04|
|runcloud-18-04|Ubuntu|25|RunCloud-18.04 on Ubuntu 18.04|
|runcloud-runcloud2004-20-04|Ubuntu|25|RunCloud-20.04 on Ubuntu 20.04|
|supabase-supabasepostgres-18-04|Ubuntu|25|Supabase Postgres 0.13.0 on Ubuntu 18.04|
|nmtec-erxes-18-04|Ubuntu|80|Erxes 0.17.6 on Ubuntu 18.04|
|fastnetmon-18-04|Ubuntu|25|FastNetMon 2.0 on Ubuntu 18.04|
|cyberscore-18-04|Ubuntu|25|CyberScore 5.0.1 on Ubuntu 18.04.3|
|shiftedit-serverwand-18-04|Ubuntu|25|ServerWand 1.0 on Ubuntu 18.04|
|ultrahorizon-uhvpn-18-04|Ubuntu|25|UH VPN 1.2.0 on Ubuntu 20.04|
|meilisas-meilisearch-10|Debian|25|MeiliSearch 0.16.0 on Debian 10 (buster)|
|helpy-18-04|Ubuntu|25|Helpy 2.4 on 18.04|
|deadcanaries-onionroutedcloud-18-04|Ubuntu|25|Onion Routed Cloud 14 on 18.04|
|dokku-18-04|Ubuntu|20|Dokku 0.17.9 on 18.04|
|mysql-18-04|Ubuntu|20|MySQL on 18.04|
|phpmyadmin-18-04|Ubuntu|20|PhpMyAdmin on 18.04|
|jenkins-18-04|Ubuntu|25|CloudBees Jenkins on 18.04|
|influxdb-18-04|Ubuntu|25|Influx TICK on 18.04|
|invoiceninja-18-04|Ubuntu|25|Invoice Ninja 1.0.0 on Ubuntu 18.0.4|
|zeromon-zabbix-18-04|Ubuntu|25|Zeromon Zabbix 4 on Ubuntu 18.04|
|lemp-18-04|Ubuntu|20|LEMP on 18.04|
|nakama-18-04|Ubuntu|25|Nakama 2.7.0 on Ubuntu 18.04|
|redash-18-04|Ubuntu|30|Redash 8.0.0 on Ubuntu 18.04|
|mattermost-18-04|Ubuntu|20|Mattermost 5.16.3 on Ubuntu 18.04|
|rethinkdb-rethinkdbfantasi-18-04|Ubuntu|25|RethinkDB (Fantasia) 2.3.7 on Ubuntu 18.04|
|openlitespeed-wp-18-04|Ubuntu|25|OpenLiteSpeed WordPress 5.3 on Ubuntu 18.04|
|sharklabs-ninjam-10-0|Debian|25|Ninjam on Debian 10.0 x64|
|workarea-18-04|Ubuntu|25|Workarea 3.5.x on Ubuntu 18.04|
|gitlab-meltano-18-04|Ubuntu|25|Meltano 1.15.0 on Ubuntu 18.04|
|rocketchat-18-04|Ubuntu|25|Rocket.Chat 2.4.9 on Ubuntu 18.04|
|reblaze-reblazewaf-18-04|Ubuntu|25|Reblaze WAF 2.12.10 on Ubuntu 18.04|
|sharklabs-nodejsquickstart-18-04|Ubuntu|25|Node.js Quickstart 1.0 on Ubuntu 18.04|
|rails-18-04|Ubuntu|20|Ruby on Rails on 18.04|
|sharklabs-foldinghome-18-04|Ubuntu|25|Folding@home 0.0.1 on Ubuntu 18.04|
|mastodon-18-04|Ubuntu|25|Mastodon 3.1.3 on Ubuntu 18.04|
|code-server-18-04|Ubuntu|25|code-server 3.0.2 on Ubuntu 18.04|
|discourse-18-04|Ubuntu|20|Discourse 2.5.0.beta3 on Ubuntu 18.04|
|mozilla-hubscloudpersona-18-04|Ubuntu|25|Hubs Cloud Personal 1.1.0 on Ubuntu 18.04|
|meltano-18-04|Ubuntu|25|Meltano 1.31.0 on Ubuntu 18.04|
|sharklabs-minecraftbedrock-20-04|Ubuntu|25|Minecraft: Bedrock Edition 1.0 on Ubuntu 20.04 (LTS)|
|botpress-18-04|Ubuntu|25|Botpress 12.9.1 on Ubuntu 18.04|
|pihole-18-04|Ubuntu|25|OpenVPN + Pihole 1.1.1 on Ubuntu 18.04|
|azuracast-18-04|Ubuntu|50|AzuraCast 0.10.3 on Ubuntu 20.04|
|ascensiosystem-onlyoffice-18-04|Ubuntu|80|ONLYOFFICE 20.02 on Ubuntu 18.04.4 LTS|
|ascensiosystemsi-onlyofficeeditor-18-04-4|Ubuntu|80|ONLYOFFICE Editors  5.5.3 on Ubuntu 18.04.4 LTS|
|revox-keplerbuilder-18-04|Ubuntu|25|Kepler Builder 1.0.10 on Ubuntu 18.04|
|directus-18-04|Ubuntu|25|Directus 8.8.1 on Ubuntu 18.04|
|jadiangaming-solderio-18-04|Ubuntu|25|Solder.io 0.7.6 on Ubuntu 18.04.5|
|lamp-20-04|Ubuntu|25|LAMP on Ubuntu 20.04|
|rethinkdb-18-04|Ubuntu|25|RethinkDB 2.4.1 on Ubuntu 18.04|
|lamp-18-04|Ubuntu|20|LAMP on Ubuntu 18.04|
|litespeedtechnol-openlitespeedwor-18-04|Ubuntu|25|OpenLiteSpeed WordPress 5.5 on Ubuntu 20.04|
|litespeedtechnol-openlitespeedrai-20-04|Ubuntu|25|OpenLiteSpeed Rails 2.7.1 on Ubuntu 20.04|
|apisnetworks-apnscp-7-7|CentOS|50|ApisCP 3.2 on CentOS 8.2|
|litespeedtechnol-openlitespeeddja-18-04|Ubuntu|25|OpenLiteSpeed Django 3.1.1 on Ubuntu 20.04|
|litespeedtechnol-openlitespeedcla-18-04|Ubuntu|25|OpenLiteSpeed ClassicPress 1.2.0 on Ubuntu 20.04|
|curiositygmbh-curiosity-16-04|Ubuntu|160|Curiosity 0.12549 on Ubuntu 16.04|
|grafana-18-04|Ubuntu|20|Grafana 7.2.0 on Ubuntu 18.04|
|wordpress-18-04|Ubuntu|25|WordPress 5.5.1 on Ubuntu 18.04|
|wordpress-20-04|Ubuntu|25|WordPress 5.5.1 on Ubuntu 20.04|
|discourse-20-04|Ubuntu|25|Discourse on Ubuntu 20.04|
|mysql-20-04|Ubuntu|25|MySQL 8.0.21 on Ubuntu 20.04|
|phpmyadmin-20-04|Ubuntu|25|PhpMyAdmin 5.0.3 on Ubuntu 20.04|
|mongodb-20-04|Ubuntu|25|MongoDB 4.4.1 on Ubuntu 20.04|
|rails-20-04|Ubuntu|25|Ruby on Rails 6.0.3.4 on Ubuntu 20.04|
|caddy-18-04|Ubuntu|25|Caddy 2.2.1 on Ubuntu 18.04|
|mongodb-18-04|Ubuntu|25|MongoDB 4.0.3 on Ubuntu 18.04|
|lemp-20-04|Ubuntu|25|LEMP on Ubuntu 20.04|
|docker-18-04|Ubuntu|25|Docker 19.03.12 on Ubuntu 18.04|
|docker-20-04|Ubuntu|25|Docker 19.03.12 on Ubuntu 20.04|
|dokku-20-04|Ubuntu|25|Dokku 0.21.4 on Ubuntu 20.04|
|harperdb-18-04|Ubuntu|25|HarperDB 2.2.2 on Ubuntu 18.04|
|helpyio-helpypro-18-04|Ubuntu|25|Helpy Pro 3.1 on Ubuntu 18.04|
|selfhostedpro-yacht-20-04|Ubuntu|25|Yacht 0.0.5-alpha on Ubuntu 20.04|
|perconamonitorin-7|CentOS|160|Percona Monitoring and Management 2 2.11.2 on CentOS 7|
|litespeedtechnol-openlitespeedjoo-20-04|Ubuntu|25|OpenLiteSpeed Joomla 3.9.22 on Ubuntu 20.04|
|cyberpanel-18-04|Ubuntu|25|CyberPanel 2.0.3 on Ubuntu 20.04|
|varnishsoftware-varnishcache-18-04|Ubuntu|25|Varnish Cache 6.0.7 on Ubuntu 18.04|
|csmm-20-04|Ubuntu|25|CSMM 1.19.4 on Ubuntu 20.04|
|acra-18-04|Ubuntu|25|Acra 0.85.0 on Ubuntu 18.04|
|alfio-7-6|CentOS|25|alf.io 2.0 on CentOS 7.6|
|chamilo-18-04|Ubuntu|25|Chamilo 1.11.10 on Ubuntu 18.04|
|opentradestatist-rstudiopkgdev-18-04|Ubuntu|25|RStudio + PkgDev 1.2 on Ubuntu 18.04|
|simplystatistics-rstudio-18-04|Ubuntu|25|RStudio 1.2 on Ubuntu 18.04|
|zabbix-7-6|CentOS|25|Zabbix 4.4.4 on CentOS 7|
|opentradestatist-rstudioh2o-18-04|Ubuntu|25|RStudio + H2O 1.2 on Ubuntu 18.04|
|metabase-18-04|Ubuntu|25|Metabase 0.34.2 on Ubuntu 18.04|
|nlnetlabs-krill-18-04|Ubuntu|25|Krill 0.6.0 on Ubuntu 18.04|
|ghost-18-04|Ubuntu|25|Ghost on Ubuntu 18.04|
|nethesis-nethserver-7|CentOS|25|NethServer 7.8.2003 on CentOS 7.x|
|iota-iotahornetnode-18-04|Ubuntu|25|IOTA Hornet Node on Ubuntu 20.04|
|microweber-18-04|Ubuntu|25|Microweber 1.1.20 on Ubuntu 18.04|
|passbolt-18-04|Ubuntu|25|Passbolt CE 2.13.5 on Ubuntu 18.04|
|opentradestatist-rstudiostan-18-04|Ubuntu|25|RStudio + Stan 1.2 on Ubuntu 18.04|
|opentradestatist-bigbluebuttonser-16-04|Ubuntu|25|BigBlueButton Server 2.2 on Ubuntu 16.04|
|livehelperchat-7-8-2003|CentOS|25|Live Helper Chat 3.55 on Centos 7.8.2003|
|deadletter-18-04|Ubuntu|25|DeadLetter Facial Recognition on 18.04|
|honeydbagent-9|Debian|25|HoneyDB Agent on Debian 9|
|nibblecomm-spotipo-18-04|Ubuntu|25|Spotipo 3.4.13 on 18.04|
|shopware-18-04|Ubuntu|25|Shopware on Ubuntu 18.04|
|48660871|20|Plesk|17.8 on CentOS 7|
|memgraph-9-7|Debian|25|Memgraph on Debian 9.7|
|vardot-varbase-18-04|Ubuntu|50|Varbase 8.7.11 on Ubuntu 18.04|
|kromit-titra-18-04|Ubuntu|25|titra 0.9.8 on Ubuntu 18.04|
|dokos-18-04|Ubuntu|80|Dokos 1.4.0 on Ubuntu 18.04|
|xcart-7|CentOS|25|X-Cart 5.4.1.4 on CentOS 7.6|
|ispsystem-ispmanagerlite-7|CentOS|25|ISPmanager Lite 5.246.0 on CentOS 7.x|
|akaunting-18-04|Ubuntu|25|Akaunting on Ubuntu 18.04|
|antmedia-16-04|Ubuntu|25|Ant Media Server Community Edition 2.1.0 on Ubuntu 18.04|
|devdojo-laravel-20-04|Ubuntu|25|Laravel 7.20.0 on Ubuntu 20.04|
|uxlens-18-04|Ubuntu|80|UXLens 0.7 on Ubuntu 18.04|
|mobilejazz-bugfender-18-04|Ubuntu|80|Bugfender 2020.2.0 on Ubuntu 18.04|
|opentradestatist-jitsiserver-18-04|Ubuntu|25|Jitsi Server 2.1-273 on Ubuntu 18.04|
|fastpanel-deb-9|Debian|25|FASTPANEL 1.9+deb10p151 on Debian 10|
|restya-restyaboard-18-04|Ubuntu|25|Restyaboard 0.6.9 on Ubuntu 18.04|
|restya-restyaboardcento-7-6|CentOS|25|Restyaboard (CentOS) 0.6.9 on CentOS 7.6|
|countly-18-04|Ubuntu|80|Countly Analytics 20.04.1 on Ubuntu 18.04|
|spatie-mailcoach-18-04|Ubuntu|25|Mailcoach 3.0 on Ubuntu 18.04|
|flashphoner-7-6|CentOS|50|Flashphoner Web Call Server 5.2.780 on CentOS 7.6|
|nodegame-18-04|Ubuntu|25|NodeGame 6.0.2 on Ubuntu 18.04|
|grandnode-18-04|Ubuntu|25|GrandNode 4.80.0 on Ubuntu 18.04|
|antmedia-antmediaserveren-16-04|Ubuntu|25|Ant Media Server Enterprise Edition 2.2.1 on Ubuntu 18.04|
|jelastic-jelasticpaas-7|CentOS|160|Jelastic PaaS 5.9-6 on Centos 7|
|plesk-7-6|CentOS|25|Plesk (CentOS) 18.0 on CentOS 7.7|
|plesk-18-04|Ubuntu|25|Plesk 18.0 on Ubuntu 18.04|
|ossn-18-04|Ubuntu|25|Open Source Social Network 5.6.0 on Ubuntu 18.04|
|mgtcommercegmbh-cloudpanel1-10-4|Debian|25|CloudPanel 1 1.0.4 on Debian 10.6|
|wikijs-18-04|Ubuntu|25|Wiki.js 2.4.107 on Ubuntu 18.04|
|analythium-shinyproxy-18-04|Ubuntu|25|ShinyProxy 2.4.0 on Ubuntu 20.04|
|analythium-opencpu-20-04|Ubuntu|25|OpenCPU 2.2 on Ubuntu 20.04|
|openfaas-18-04|Ubuntu|25|OpenFaaS on Ubuntu 18.04|
|thingsboard-18-04|Ubuntu|20|ThingsBoard CE on Ubuntu 18.04|
|thingsboardpe-18-04|Ubuntu|20|ThingsBoard PE on Ubuntu 18.04|
|openlitespeed-node-18-04|Ubuntu|25|OpenLiteSpeed NodeJS 10.15.3 on Ubuntu 18.04|
|openlitespeed-django-18-04|Ubuntu|25|OpenLiteSpeed Django 2.2.3 on Ubuntu 18.04|
|bcoin-18-04|Ubuntu|20|bcoin on 18.04|
|cpanel-7-6|CentOS|25|cPanel & WHM® 84.0.14 on CentOS 7.6|
|restyaboard-16-04|Ubuntu|25|Restyaboard 0.6.8 on Ubuntu 16.04|
|restyaboard-7-6|CentOS|25|Restyaboard (CentOS) 0.6.8 on CentOS 7.6|
|sharklabs-pythondjangoquic-18-04|Ubuntu|25|Python/Django Quickstart 1.1 on Ubuntu 18.04|
|ten7-computingforcovi-18-04-4|Ubuntu|60|Computing for COVID 3 on Ubuntu 18.04.4 LTS|
|openvpn-18-04|Ubuntu|25|OpenVPN Access Server 2.8.5 on Ubuntu 18.04|
|cpanel-cpanelwhm-7-6|CentOS|25|cPanel & WHM® 90.0.15 on CentOS 7.6|
|nknfullnode-18-04|Ubuntu|25|NKN Commercial 2.0 on Ubuntu 18.04|
|prometheus-18-04|Ubuntu|20|Prometheus 2.9.2 on Ubuntu 18.04|
|onjection-jenkins-16-04|Ubuntu|25|Onjection Jenkins 2.164.3 on Ubuntu 16.04|
|flexify-18-04|Ubuntu|20|Flexify 2.8.1 on Ubuntu 18.04|
|vitalpointz-7-6|CentOS|25|vitalpointz IoT Core Lite 1.2.0 on CentOS 7.6|
|hasura-18-04|Ubuntu|25|Hasura GraphQL on Ubuntu 18.04|
|erpnext-18-04|Ubuntu|160|ERPNext 12.5.0 on Ubuntu 18.04|
|bagisto-18-04|Ubuntu|25|Bagisto on 18.04|
|seknox-trasa-20-04|Ubuntu|25|TRASA 1.1.2 on Ubuntu 20.04|
|zoomadmin-18-04|Ubuntu|25|ZoomAdmin 2.0.1 on Ubuntu 18.04.03|
|nodejs-20-04|Ubuntu|20|NodeJS 12.18.0 on Ubuntu 20.04|
|django-20-04|Ubuntu|25|Django 2.2.12 on Ubuntu 20.04|
|traccar-20-04|Ubuntu|25|Traccar 4.10 on Ubuntu 20.04|
