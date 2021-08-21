# Baya-Weaver

Online Website Builder

# Back Story

Inspired by the engineering that is Wix.com and Wordpress, I ought to understand how something as complex as a Website builder is built. A website that makes a website lol. 

So I started off searching on Youtube and Stackoverflow, which was not as successful as I thought it would be. I eventually came across an answer by Sunday Ironfoot on StackOverflow, which he says
<p>
"You've effectively been given the task of writing a full blown Content Management System. This is a mammoth task that would probably take a lone developer anything from 6 - 24 months to build depending on experience (this based on development time of other CMS' on the market). For instance, the developers of Umbraco (an Open source ASP.NET CMS) are busy porting their CMS over to ASP.NET MVC, work started around beginning of this year and is not expected to be built until middle of next year, and they're some of the most talented devs in the industry." 
</p>

At this point I became more serious about building a website builder, and I had to do it over the weekend beccause I was still working on Cloud Winterstore which was unfinish. 
An answer above Sunday Ironfoot by Morfildur stated 

<p style="font-style: italic;">
"A simple solution would be to have several base-templates with placeholders that get filled with content/other templates later. Then you provide the users with a simple way to define page headers and page_contents, i.e. the first might just be a textbox, the content is filled by using something like TinyMCE. If necessary, the clients can use other placeholders in the content, but that might not be neccessary.After that you just add an auto-generated menu, create the logic that replaces the placeholders with the user-entered content (something along the lines of template.Content = template.Content.Replace("{page_content}", customer.Pages['foo'].GetTemplateContent("page_content")); )and maybe add a CSS stylesheet with color and font settings provided by the customers. The most complex part is the backend and user-authentification. This solution is simple to implement and has no real flexibility at all but it allows customers to quickly write a few texts and add some fancy images without having to care about anything else. To persist color settings, write them into the database and create a new CSS stylesheet everytime they are changed. For other content just use a Database table "content" with the columns "key" and "value" and you might want to generate static HTML pages on every change."

With Morfildur answer I was able to craft up a model of a website builder that is able to

(1) Edit DOM Elements

(2) Support multiple users

(3) Allow preview of the page

(4) Allow loading of prebuilt templates

(5) Automatic saving of changes

# Preview

https://user-images.githubusercontent.com/63599157/130330031-5315e201-8e6b-4369-8508-978924ed8794.mp4

https://user-images.githubusercontent.com/63599157/130330058-afeda5cd-9a85-4363-8577-f5d4af6e386a.mp4

https://user-images.githubusercontent.com/63599157/130330060-d1641faf-125f-4599-9d28-6ffdb00c22cc.mp4

https://user-images.githubusercontent.com/63599157/130330065-8e31d8dc-1c63-469a-9fd3-51256dba4c40.mp4

https://user-images.githubusercontent.com/63599157/130330134-d5175dce-8bb4-475a-af10-bcfe57f8de58.mp4

# About

Baya Weaver is a model of an online website builder, that support the following functions
(1) Edit DOM Elements
(2) Support multiple users
(3) Allow preview of the page
(4) Allow loading of prebuilt templates
(5) Automatic saving of changes

It is built around python's django framework, Vanilla JS, CSS3 and HTML.

# References 
  
Morfildur and Sunday Ironfoot's answers
  
https://stackoverflow.com/questions/3059592/creating-a-website-builder-how-would-i-architect-it

