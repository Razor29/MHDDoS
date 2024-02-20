# MHDDoS Parallel Script Runner and Scheduler

## Description

The attack Script is a Python tool designed to expand and enhance MHDDoS but allowing the user to run multiple instaces simultaniously with different attack vectors, or schedule many different concurrent attacks to a specified URL and it adds monitoring outpyt such as  CPU usage, memory usage, upload speed, and packets sent per second. It supports scheduling jobs to run at specific times, executing multiple instances with different configurations, and customizing the number of threads, requests, and duration for each job.

## Prerequisites

- Python 3.x
- `psutil` library
- `schedule` library

To install the required Python libraries, run:

```bash
pip install psutil schedule
```

## Setup

1. **Download the Script**: Download `attack.py` to your base directory of MHDDoS.

## Usage

The script is executed via the command line with several optional arguments to customize its behavior.

### Arguments

- `time`: Specify `now` to run the job immediately or `schedule` to set up scheduled jobs (default: `schedule`).
- `--threads`: The number of threads to use (default: 2).
- `--requests`: The number of requests to send per thread (default: 100).
- `--seconds`: The duration in seconds for which the job should run (default: 300).
- `--url`: The URL to send requests to (default: `https://notreal.notnet`).
- `--instances`: The number of instances to run (default: 2).
- `--http`: name of the text file containing the HTTP proxie list  (default: `http.txt`).
- `--method`: Comma-separated list of HTTP methods to use, matching the number of instances (default: GET, GET). The allowed types are: `DOWNLOADER, DYN, BOMB, STRESS, XMLRPC, GET, HEAD, AVB, POST, SLOW, BOT, STOMP, CFB, APACHE, BYPASS, GSB, TOR, NULL, DGB, RHEX, OVH, PPS, CFBUAM, EVEN, COOKIE, KILLER`.
- 
### Running the Script

To execute the script with the default settings, simply navigate to the directory where the script is located and run:

```bash
python attack.py
```

#### Example 1: Run Immediately with Custom Configuration

To run the job immediately with custom configurations, use the `now` argument and specify other desired parameters:

```bash
python attack.py now --threads 4 --requests 200 --seconds 60 --url https://notreal.notreal --instances 2 --http_file http.txt --methods GET,POST
```

This command runs the script immediately with 4 threads, 200 requests, for 60 seconds, against `https://notreal.notreal`, in 2 instances, using the HTTP proxies from `http.txt`.

To use the script without proxies default to http.txt, to use proxies choose another filename and it will be created.

#### Example 2: Schedule Jobs

scheduled job's require chnaging argument default within attack.py and changing the jobs_to_run variable which is curently 
```bash
    jobs_to_run = [
        # Assuming the format is (methods, threads, requests, seconds, instances)
        ("EVEN,GET", 70, 1, 60, 2),
        ("EVEN,GET", 50, 100, 580, 2),
        ("HEAD,HEAD", 50, 100, 600, 2),
    ]
```

This current configuration runs 3 concurent attacks of 60 seconds, 580 and 600 each with 2 instances, between 70 and 50 threads and 1 - 100 request per thread

### Monitoring Output

The script logs its output to the console, including start times for jobs, CPU usage, memory usage, upload speed, and packets sent per second. Ensure the console or log viewer is open to monitor these metrics.

## Original Readme

<p align="center"><img src="https://cdn.discordapp.com/attachments/938175699326484490/948263435412598864/unknown_2.png" width="400px" height="150px" alt="ddos"></p>

<h1 align="center">MHDDoS - DDoS Attack Script With 56 Methods</h1>
<em><h5 align="center">(Programming Language - Python 3)</h5></em>

<p align="center">
<a href="#"><img alt="MH-DDoS forks" src="https://img.shields.io/github/forks/MatrixTM/MHDDoS?style=for-the-badge"></a>
<a href="#"><img alt="MH-DDoS last commit (main)" src="https://img.shields.io/github/last-commit/MatrixTM/MHDDoS/main?color=green&style=for-the-badge"></a>
<a href="#"><img alt="MH-DDoS Repo stars" src="https://img.shields.io/github/stars/MatrixTM/MHDDoS?style=for-the-badge&color=yellow"></a>
<a href="#"><img alt="MH-DDoS License" src="https://img.shields.io/github/license/MatrixTM/MHDDoS?color=orange&style=for-the-badge"></a>
<a href="https://github.com/MatrixTM/MHDDoS/issues"><img alt="MatrixTM issues" src="https://img.shields.io/github/issues/MatrixTM/MHDDoS?color=purple&style=for-the-badge"></a>
  
<p align="center">Please Don't Attack websites without the owners consent.</p>

<p align="center"><img src="https://i.imgur.com/aNrHJcA.png" width="1078" height="433" alt="POWER"></p>
<p align="center"><img src="https://i.imgur.com/4Q7v2wn.png" width="1078" height="296" alt="SCRIPT"></p>

## Features And Methods

 * 💣 Layer7

   * <img src="https://img.icons8.com/cotton/344/domain.png" width="16" height="16" alt="get"> GET | GET Flood
   * <img src="https://cdn0.iconfinder.com/data/icons/database-storage-5/60/server__database__fire__burn__safety-512.png" width="16" height="16" alt="post"> POST | POST Flood
   * <img src="https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/OVH_Logo.svg/1200px-OVH_Logo.svg.png" width="16" height="16" alt="ovh"> OVH | Bypass OVH
   * <img src="https://cdn-icons-png.flaticon.com/512/1691/1691948.png" width="16" height="16" alt="ovh"> RHEX | Random HEX
   * <img src="https://cdn-icons-png.flaticon.com/512/4337/4337972.png" width="16" height="16" alt="ovh"> STOMP | Bypass chk_captcha
   * <img src="https://cdn.iconscout.com/icon/premium/png-256-thumb/cyber-bullying-2557797-2152371.png" width="16" height="16" alt="stress"> STRESS | Send HTTP Packet With High Byte 
   * <img src="https://pbs.twimg.com/profile_images/1351562987224641544/IKb4q_yd_400x400.jpg" width="16" height="16" alt="dyn"> DYN | A New Method With Random SubDomain
   * <img src="https://cdn-icons-png.flaticon.com/512/6991/6991643.png" width="16" height="16" alt="downloader"> DOWNLOADER | A New Method of Reading data slowly
   * <img src="https://cdn2.iconfinder.com/data/icons/poison-and-venom-fill/160/loris2-512.png" width="16" height="16" alt="slow"> SLOW | Slowloris Old Method of DDoS
   * <img src="https://lyrahosting.com/wp-content/uploads/2020/06/ddos-how-work-icon.png" width="16" height="16" alt="head"> HEAD | https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD
   * <img src="https://img.icons8.com/plasticine/2x/null-symbol.png" width="16" height="16" alt="null"> NULL | Null UserAgent and ...
   * <img src="https://i.pinimg.com/originals/03/2e/7d/032e7d0755cd511c753bcb6035d44f68.png" width="16" height="16" alt="cookie"> COOKIE | Random Cookie PHP 'if (isset($_COOKIE))'
   * <img src="https://cdn0.iconfinder.com/data/icons/dicticons-files-folders/32/office_pps-512.png" width="16" height="16" alt="pps"> PPS |  Only 'GET / HTTP/1.1\r\n\r\n'
   * <img src="https://cdn3.iconfinder.com/data/icons/internet-security-14/48/DDoS_website_webpage_bomb_virus_protection-512.png" width="16" height="16" alt="even"> EVEN | GET Method with more header
   * <img src="https://projectshield.withgoogle.com/static/icons/favicon.ico" width="16" height="16" alt="googleshield"> GSB | Google Project Shield Bypass
   * <img src="https://seeklogo.com/images/D/ddos-guard-logo-CFEFCA409C-seeklogo.com.png" width="16" height="16" alt="DDoSGuard"> DGB | DDoS Guard Bypass
   * <img src="https://i.imgur.com/bGL8qfw.png" width="16" height="16" alt="ArvanCloud"> AVB | Arvan Cloud Bypass
   * <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/1024px-Google_%22G%22_Logo.svg.png" width="16" height="16" alt="Google bot"> BOT | Like Google bot
   * <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Apache_HTTP_Server_Logo_%282016%29.svg/1000px-Apache_HTTP_Server_Logo_%282016%29.svg.png" width="16" height="16" alt="Apache Webserver"> APACHE | Apache Expliot
   * <img src="https://icon-library.com/images/icon-for-wordpress/icon-for-wordpress-16.jpg" width="16" height="16" alt="wordpress expliot"> XMLRPC | WP XMLRPC expliot (add /xmlrpc.php)
   * <img src="https://techcrunch.com/wp-content/uploads/2019/06/J2LlHqT3qJl0bG9Alpgc-1-730x438.png?w=730" width="16" height="16" alt="CloudFlare"> CFB | CloudFlare Bypass
   * <img src="https://techcrunch.com/wp-content/uploads/2019/06/J2LlHqT3qJl0bG9Alpgc-1-730x438.png?w=730" width="16" height="16" alt="CloudFlare UnderAttack Mode"> CFBUAM | CloudFlare Under Attack Mode Bypass
   * <img src="http://iclouddnsbypass.com/wp-content/uploads/2015/02/iCloudDNSBypassServer.ico" width="16" height="16" alt="bypass"> BYPASS |  Bypass Normal AntiDDoS
   * <img src="https://cdn-icons-png.flaticon.com/512/905/905568.png" width="16" height="16" alt="bypass"> BOMB |  Bypass with codesenberg/bombardier
   * 🔪 KILLER | Run many threads to kill a target
   * 🧅 TOR | Bypass onion website


* 🧨 Layer4: 
  * <img src="https://raw.githubusercontent.com/kgretzky/pwndrop/master/media/pwndrop-logo-512.png" width="16" height="16" alt="tcp"> TCP | TCP Flood Bypass
  * <img src="https://styles.redditmedia.com/t5_2rxmiq/styles/profileIcon_snoob94cdb09-c26c-4c24-bd0c-66238623cc22-headshot.png" width="16" height="16" alt="udp"> UDP | UDP Flood Bypass
  * <img src="https://cdn-icons-png.flaticon.com/512/1918/1918576.png" width="16" height="16" alt="syn"> SYN | SYN Flood
  * <img src="https://cdn-icons-png.flaticon.com/512/1017/1017466.png" width="16" height="16" alt="cps"> CPS | Open and close connections with proxy
  * <img src="https://icon-library.com/images/icon-ping/icon-ping-28.jpg" width="16" height="16" alt="icmp"> ICMP | Icmp echo request flood (Layer3)
  * <img src="https://s6.uupload.ir/files/1059643_g8hp.png" width="16" height="16" alt="connection"> CONNECTION | Open connection alive with proxy
  * <img src="https://ia803109.us.archive.org/27/items/source-engine-video-projects/source-engine-video-projects_itemimage.png" width="16" height="16" alt="vse"> VSE | Send Valve Source Engine Protocol
  * <img src="https://mycrackfree.com/wp-content/uploads/2018/08/TeamSpeak-Server-9.png" width="16" height="16" alt="teamspeak 3"> TS3 | Send Teamspeak 3 Status Ping Protocol
  * <img src="https://cdn2.downdetector.com/static/uploads/logo/75ef9fcabc1abea8fce0ebd0236a4132710fcb2e.png" width="16" height="16" alt="fivem"> FIVEM | Send FiveM Status Ping Protocol
  * <img src="https://cdn.iconscout.com/icon/free/png-512/redis-4-1175103.png" width="16" height="16" alt="mem"> MEM | Memcached Amplification
  * <img src="https://lyrahosting.com/wp-content/uploads/2020/06/ddos-attack-icon.png" width="16" height="16" alt="ntp"> NTP | NTP Amplification
  * <img src="https://cdn-icons-png.flaticon.com/512/4712/4712139.png" width="16" height="16" alt="mcbot"> MCBOT | Minecraft Bot Attack
  * <img src="https://cdn.icon-icons.com/icons2/2699/PNG/512/minecraft_logo_icon_168974.png" width="16" height="16" alt="minecraft"> MINECRAFT | Minecraft Status Ping Protocol
  * <img src="https://cdn.icon-icons.com/icons2/2699/PNG/512/minecraft_logo_icon_168974.png" width="16" height="16" alt="minecraft pe"> MCPE | Minecraft PE Status Ping Protocol
  * <img src="https://cdn-icons-png.flaticon.com/512/2653/2653461.png" width="16" height="16" alt="dns"> DNS | DNS Amplification
  * <img src="https://lyrahosting.com/wp-content/uploads/2020/06/ddos-attack-icon.png" width="16" height="16" alt="chargen"> CHAR | Chargen Amplification
  * <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRct5OvjSCpUftyRMm3evgdPOa-f8LbwJFO-A&usqp=CAU" width="16" height="16" alt="cldap"> CLDAP | Cldap Amplification
  * <img src="https://help.apple.com/assets/6171BD2C588E52621824409D/6171BD2D588E5262182440A4/en_US/8b631353e070420f47530bf95f1a7fae.png" width="16" height="16" alt="ard"> ARD | Apple Remote Desktop Amplification
  * <img src="https://www.tenforums.com/geek/gars/images/2/types/thumb__emote__esktop__onnection.png" width="16" height="16" alt="rdp"> RDP |  Remote Desktop Protocol Amplification

* ⚙️ Tools - Run With 
`
python3 start.py tools
`
  * 🌟 CFIP | Find Real IP Address Of Websites Powered By Cloudflare
  * 🔪 DNS | Show DNS Records Of Sites
  * 📍  TSSRV | TeamSpeak SRV Resolver
  * ⚠  PING | PING Servers
  * 📌 CHECK | Check If Websites Status
  * 😎 DSTAT | That Shows Bytes Received, bytes Sent and their amount

* 🎩 Other
  * ❌ STOP | STOP All Attacks
  * 🌠 TOOLS | Console Tools
  * 👑 HELP | Show Usage Script


<h1 align="center">
Our social's💻
</h2> 

<div align="center">
   <img src="https://icon-library.com/images/github-icon-vector/github-icon-vector-27.jpg" width="96" height="96" alt="github" />
   <img src="https://brandlogos.net/wp-content/uploads/2021/11/discord-logo.png"  width="96" height="96" alt="discord" />
   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/2048px-Telegram_logo.svg.png" width="96" height="96" alt="telegram" />
</div>

 * [Matrix Team Telegram group](https://t.me/DD0SChat)
 * [Matrix community Telegram channel](https://t.me/MatrixORG)
 * [GitHub](https://github.com/MatrixTM)
### If u Like the project, leave a star on the repository!

## Downloads

You can download it from [GitHub Releases](https://github.com/MatrixTM/MHDDoS/releases)

### Getting Started

**Requirements**

* [dnspython](https://github.com/rthalley/dnspython)
* [cfscrape](https://github.com/Anorov/cloudflare-scrape)
* [impacket](https://github.com/SecureAuthCorp/impacket)
* [requests](https://github.com/psf/requests)
* [Python3][python3]
* [PyRoxy](https://github.com/MatrixTM/PyRoxy)
* [icmplib](https://github.com/ValentinBELYN/icmplib)
* [certifi](https://github.com/certifi/python-certifi)
* [psutil](https://github.com/giampaolo/psutil)
* [yarl](https://github.com/aio-libs/yarl)
---

**Videos**

* Aparat: https://www.aparat.com/v/bHcP9
* YouTube : Coming soon...

**Tutorial**

* Aparat : https://aparat.com/v/XPn5Z
* YouTube : Coming soon...
---

## Documentation

You can read it from [GitHub Wiki](https://github.com/MatrixTM/MHDDoS/wiki)

**Clone and Install Script**

```shell script
git clone https://github.com/MatrixTM/MHDDoS.git
cd MHDDoS
pip install -r requirements.txt
```

**One-Line Installing on Fresh VPS**

```shell script
apt -y update && apt -y install curl wget libcurl4 libssl-dev python3 python3-pip make cmake automake autoconf m4 build-essential git && git clone https://github.com/MatrixTM/MHDDoS.git && cd MH* && pip3 install -r requirements.txt
```

