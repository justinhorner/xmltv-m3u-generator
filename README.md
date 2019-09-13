# xmltv-m3u-generator

This program will generate an m3u file based on xmltv data.

* The program has only been tested against xmltv data generated via [Zap2It](https://tvlistings.zap2it.com/?aid=gapzap) using the perl program [zap2xml](http://zap2xml.awardspace.info).
* The program generates m3u links based on what I needed to output for my hdhomerun.  The url generated is in the following format:
  * `http://192.168.0.1:5004/auto/v1.1`
    * With `http://192.168.1.1:5004/auto/` being the url the hdhomerun needed
    * And `v1.1` being the path used for the channel 

I made this script to easily generate an m3u file using tv guide data for OTA tv.  I found while I could easily generate tv guide data using zap2it, generating an actual list of m3u links (from my hdHomeRun device) was a pretty manual process.  Plus, with the ability to favorite in Zap2It made it easy to filter out channels I didn't care to see in my guide.
 

## Config file

* xmlFilePath: the path of your xmltv xml file
* hdhomerunUrlPrefix: this is the hdhomerun channel url, minus the channel portion of the path. e.g. "1.1"
* m3uFilename: filename you want to use for the generated m3u file
