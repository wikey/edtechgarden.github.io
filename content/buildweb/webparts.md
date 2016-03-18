Title: Parts of a website, parts of the web           
Date: 2016-03-14 16:00
Category: buildweb
Tags: session1
Slug: webparts

*[Back to Session 1](./session1.html)*

## What is a webpage?

Many of the metaphors related to web pages treat them as places. You "visit" a site, you "follow" a link, even we are talking about "reclaiming" our own corner of the web like it were an occupied land. These metaphors help capture the experience of using the internet but they mask the real nature of that network. 

So, if webpages are not places, what exactly are they? Webpages are documents. 

When you load a website your computer goes out and asks the computer with all the documents for that site for the one that matches the address you typed and then your web browser opens and displays the document just like you would open PDF or spreadsheet. If everything works well your computer downloads and opens the documents so quickly that it feels like movement through a virtual space instead of just opening a series of documents really fast. The only real differences between a website and documents you might be more familiar with, like word processor or slide show ones, are the particular formats used to write them and the fact that you are getting them from another computer. 

## The parts of a website 

The actual document that makes up a website is written in a couple of parts that each have their own special formatting. The real content of the page, all the writing, the structure of the document, where images should go, etc, uses HTML formatting, which uses combinations of normal letters and symbols to indicate formatting. For example, if you want some words to be emphasized on a web page, instead of italicizing them, you would write: 

~~~
<em>emphasize me!</em>
~~~

A second part of the website document contains all the information about how to style this html, what colors to use, whether words marked with em's should be displayed as italics or perhaps in bold, how big the headings should be, that kind of thing. This second part uses CSS formatting. 

The final part is optional and contains all the interactive elements more complicated than a link, things like animations. This last part can be written in any number of programming languages though the most common one online is JavaScript or "js". All these parts of the document live on a web server, which is just a computer that has been set up to send you a document when you go to the right web address and to run the script portions of a site if there are any. 

## How to share your site online

At the most basic level, having your own website means three things: having a document you want people to see when they visit, this is the site itself, having a computer connected to the internet and configured to give out that document, this is the web server, and having a way for people to find your computer, this is the domain name like "p2pu.org" or "edtechgarden.org" that appears in the browser location bar. When you sign up with Reclaim Hosting, or most any web hosting provider, you are paying to register your own domain name, and for the use of the hosting company's computer for giving out your web site document. 

## Further reading / Additional resources

* Watch [HTML &amp; how the web works (briefly)][1] (~8 mins)
* Read: [The basics of HTML][2] (W3C Web Education Community Group)
* Dive in: [HTML &amp; CSS course][3] (Code academy)


  [1]: https://www.youtube.com/watch?v=78TDg6_g3cM&amp;feature=youtu.be
  [2]: https://www.w3.org/community/webed/wiki/The_basics_of_HTML
  [3]: https://www.codecademy.com/learn/web
