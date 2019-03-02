<script type="text/javascript">

 
 var currenttime = 'February 20, 2019 19:58:58' ;//PHP method of getting server date

///////////Stop editting here/////////////////////////////////

var montharray=new Array("January","February","March","April","May","June","July","August","September","October","November","December")
var serverdate=new Date(currenttime)

function padlength(what){
var output=(what.toString().length==1)? "0"+what : what
return output
}

function displaytime(){
 
serverdate.setSeconds(serverdate.getSeconds()+1)
var datestring=montharray[serverdate.getMonth()]+" "+padlength(serverdate.getDate())+", "+serverdate.getFullYear()
var timestring=padlength(serverdate.getHours())+":"+padlength(serverdate.getMinutes())+":"+padlength(serverdate.getSeconds())
document.getElementById("servertime").innerHTML=datestring+" "+timestring
}

window.onload=function(){
setInterval("displaytime()", 1000)
}

</script>

<!DOCTYPE html>
<html  dir="ltr" lang="en" xml:lang="en">
<head>
    <title>Site policy agreement</title>
    <link rel="shortcut icon" href="https://lms.nust.edu.pk/portal/theme/image.php/nust/theme/1548661015/favicon" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="moodle, Site policy agreement" />
<link rel="stylesheet" type="text/css" href="https://lms.nust.edu.pk/portal/theme/yui_combo.php?3.7.3/build/cssreset/reset-min.css&amp;3.7.3/build/cssfonts/fonts-min.css&amp;3.7.3/build/cssgrids/grids-min.css&amp;3.7.3/build/cssbase/base-min.css" /><script type="text/javascript" src="https://lms.nust.edu.pk/portal/theme/yui_combo.php?3.7.3/build/simpleyui/simpleyui-min.js&amp;3.7.3/build/loader/loader-min.js"></script><script id="firstthemesheet" type="text/css">/** Required in order to fix style inclusion problems in IE with YUI **/</script><link rel="stylesheet" type="text/css" href="https://lms.nust.edu.pk/portal/theme/styles.php/nust/1548661015/all" />
<script type="text/javascript">
//<![CDATA[
var M = {}; M.yui = {};
var moodleConfigFn = function(me) {var p = me.path, b = me.name.replace(/^moodle-/,'').split('-', 3), n = b.pop();if (/(skin|core)/.test(n)) {n = b.pop();me.type = 'css';};me.path = b.join('-')+'/'+n+'/'+n+'.'+me.type;};
var galleryConfigFn = function(me) {var p = me.path,v=M.yui.galleryversion,f;if(/-(skin|core)/.test(me.name)) {me.type = 'css';p = p.replace(/-(skin|core)/, '').replace(/\.js/, '.css').split('/'), f = p.pop().replace(/(\-(min|debug))/, '');if (/-skin/.test(me.name)) {p.splice(p.length,0,v,'assets','skins','sam', f);} else {p.splice(p.length,0,v,'assets', f);};} else {p = p.split('/'), f = p.pop();p.splice(p.length,0,v, f);};me.path = p.join('/');};
var yui2in3ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin');}};
YUI_config = {"base":"https:\/\/lms.nust.edu.pk\/portal\/lib\/yuilib\/3.7.3\/build\/","comboBase":"https:\/\/lms.nust.edu.pk\/portal\/theme\/yui_combo.php?","combine":true,"filter":"","insertBefore":"firstthemesheet","modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/lms.nust.edu.pk\/portal\/lib\/javascript.php\/1548663895\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","moodle-core_filepicker"]},"core_dock":{"name":"core_dock","fullpath":"https:\/\/lms.nust.edu.pk\/portal\/lib\/javascript.php\/1548663895\/blocks\/dock.js","requires":["base","node","event-custom","event-mouseenter","event-resize"]}},"groups":{"moodle":{"name":"moodle","base":"https:\/\/lms.nust.edu.pk\/portal\/theme\/yui_combo.php?moodle\/1548663895\/","comboBase":"https:\/\/lms.nust.edu.pk\/portal\/theme\/yui_combo.php?","combine":true,"filter":"","ext":false,"root":"moodle\/1548663895\/","patterns":{"moodle-":{"group":"moodle","configFn":moodleConfigFn}}},"local":{"name":"gallery","base":"https:\/\/lms.nust.edu.pk\/portal\/lib\/yui\/gallery\/","comboBase":"https:\/\/lms.nust.edu.pk\/portal\/theme\/yui_combo.php?","combine":true,"filter":"","ext":false,"root":"gallery\/","patterns":{"gallery-":{"group":"gallery","configFn":galleryConfigFn}}},"yui2":{"base":"https:\/\/lms.nust.edu.pk\/portal\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/lms.nust.edu.pk\/portal\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui2in3ConfigFn}}}}};
M.yui.loader = {modules: {}};
M.cfg = {"wwwroot":"https:\/\/lms.nust.edu.pk\/portal","sesskey":"vkjztrzmoD","loadingicon":"https:\/\/lms.nust.edu.pk\/portal\/theme\/image.php\/nust\/core\/1548661015\/i\/loading_small","themerev":"1548661015","slasharguments":1,"theme":"nust","jsrev":"1548663895","svgicons":true};
//]]>
</script>
<script type="text/javascript" src="https://lms.nust.edu.pk/portal/lib/javascript.php/1548663895/lib/javascript-static.js"></script>
<script type="text/javascript" src="https://lms.nust.edu.pk/portal/theme/javascript.php/nust/1548661015/head"></script>
</head>

<body id="page-user-policy" class=" path-user safari dir-ltr lang-en yui-skin-sam yui3-skin-sam lms-nust-edu-pk--portal pagelayout-base course-1 context-1 content-only has_custom_menu">
<div class="skiplinks"><a class="skip" href="#maincontent">Skip to main content</a></div>
<script type="text/javascript">
//<![CDATA[
document.body.className += ' jsenabled';
//]]>
</script>


<div id="page">
    <div id="page-header">
        <div id="page-header-wrapper" class="wrapper clearfix">
                <h1 class="headermain inside">NUST LMS Portal</h1>
                <div class="headermenu"><div class="logininfo">You are currently using guest access (<a href="https://lms.nust.edu.pk/portal/login/index.php">Login</a>)</div>                </div>
        </div>
    </div>

     <div id="custommenuwrap"><div id="custommenu"><div id="custom_menu_1" class="yui3-menu yui3-menu-horizontal javascript-disabled"><div class="yui3-menu-content"><ul><li><a class="yui3-menu-label" title="Navigation" href="#cm_submenu_1">Navigation</a><div id="cm_submenu_1" class="yui3-menu custom_menu_submenu"><div class="yui3-menu-content"><ul><li><a class="yui3-menu-label" title="Profile Settings" href="#cm_submenu_2">Profile Settings</a><div id="cm_submenu_2" class="yui3-menu custom_menu_submenu"><div class="yui3-menu-content"><ul><li class="yui3-menuitem"><a class="yui3-menuitem-content" title="Edit Profile" href="https://lms.nust.edu.pk/portal/user/editadvanced.php">Edit Profile</a></li><li class="yui3-menuitem"><a class="yui3-menuitem-content" title="Change Password" href="https://lms.nust.edu.pk/portal/login/change_password.php?id=1">Change Password</a></li><li class="yui3-menuitem"><a class="yui3-menuitem-content" title="Messaging" href="https://lms.nust.edu.pk/portal/message/index.php">Messaging</a></li></ul></div></div></li><li class="yui3-menuitem"><a class="yui3-menuitem-content" title="Site News" href="https://lms.nust.edu.pk/portal/mod/forum/view.php?id=2">Site News</a></li><li class="yui3-menuitem"><a class="yui3-menuitem-content" title="Site home" href="https://lms.nust.edu.pk/portal/?redirect=0">Site home</a></li><li class="yui3-menuitem"><a class="yui3-menuitem-content" title="My Home" href="https://lms.nust.edu.pk/portal/my/">My Home</a></li></ul></div></div></li><li class="yui3-menuitem"><a class="yui3-menuitem-content" title="Troubleshooting" href="https://lms.nust.edu.pk/portal/mod/forum/view.php?id=26">Troubleshooting</a></li><li class="yui3-menuitem"><a class="yui3-menuitem-content" title="FAQ" href="https://lms.nust.edu.pk/portal/mod/data/view.php?id=2901">FAQ</a></li><li class="yui3-menuitem"><a class="yui3-menuitem-content" title="Suggestions" href="https://lms.nust.edu.pk/portal/mod/forum/view.php?id=3623">Suggestions</a></li><li class="yui3-menuitem"><a class="yui3-menuitem-content" title="Contact us" href="https://lms.nust.edu.pk/portal/mod/page/view.php?id=14002">Contact us</a></li><li class="yui3-menuitem"><a class="yui3-menuitem-content" title="Training" href="https://lms.nust.edu.pk/portal/mod/url/view.php?id=32049">Training</a></li><li class="yui3-menuitem"><a class="yui3-menuitem-content" title="Downloads" href="https://lms.nust.edu.pk/portal/mod/page/view.php?id=115333">Downloads</a></li><li class="yui3-menuitem"><a class="yui3-menuitem-content" title="Digital Library" href="https://lms.nust.edu.pk/portal/mod/url/view.php?id=91120">Digital Library</a></li></ul></div></div> </div> <div id="servertime"  style=" float:right;position:relative;margin-top: -23; margin-right:22px; color: #FFF"></div></div>


                    <div class="navbar">
                <div class="wrapper clearfix">
                    <div class="breadcrumb"><span class="accesshide">Page path</span><ul role="navigation"><li><a title="Home" href="https://lms.nust.edu.pk/portal/">Home</a></li><li> <span class="accesshide " ><span class="arrow_text">/</span>&nbsp;</span><span class="arrow sep">&#x25BA;</span> <span tabindex="0">Site policy agreement</span></li></ul></div>
                    <div class="navbutton"> </div>
                </div>
            </div>
        			

<!-- END OF HEADER -->
<div id="page-content-wrapper" class="wrapper clearfix">
    <div id="page-content">
        <div id="region-main-box">
            <div id="region-post-box">

                <div id="region-main-wrap">
                    <div id="region-main">
                        <div class="region-content">
                                                        <div role="main"><span id="maincontent"></span><h2 class="main">Site policy agreement</h2><div class="noticebox"><div class="resourcecontent resourcegeneral">
  <object id="resourceobject" data="https://lms.nust.edu.pk/lms/file.php/1/policy.html" type="text/html"  width="800" height="600">
    <param name="src" value="https://lms.nust.edu.pk/lms/file.php/1/policy.html" />
    <a href="https://lms.nust.edu.pk/lms/file.php/1/policy.html" onclick="this.target='_blank'">Link to site policy agreement</a>
  </object>
</div></div><div id="notice" class="box generalbox"><p>You must agree to this policy to continue using this site.  Do you agree?</p><div class="buttons"><div class="singlebutton"><form method="post" action="policy.php"><div><input type="submit" value="Yes" /><input type="hidden" name="agree" value="1" /><input type="hidden" name="sesskey" value="vkjztrzmoD" /></div></form></div><div class="singlebutton"><form method="post" action="https://lms.nust.edu.pk/portal/login/logout.php"><div><input type="submit" value="No" /><input type="hidden" name="agree" value="0" /><input type="hidden" name="sesskey" value="vkjztrzmoD" /></div></form></div></div></div></div>                                                    </div>
                    </div>
                </div>

                
                
            </div>
        </div>
    </div>
</div>

    
<!-- START OF FOOTER -->
        <div id="page-footer" class="wrapper">
        <p class="helplink"></p>
        <div class="logininfo">You are currently using guest access (<a href="https://lms.nust.edu.pk/portal/login/index.php">Login</a>)</div><div class="homelink"><a href="https://lms.nust.edu.pk/portal/">Home</a></div>    </div>
    </div>
<script type="text/javascript" src="https://lms.nust.edu.pk/portal/theme/javascript.php/nust/1548661015/footer"></script>
<script type="text/javascript">
//<![CDATA[
M.str = {"moodle":{"lastmodified":"Last modified","name":"Name","error":"Error","info":"Information","cancel":"Cancel","yes":"Yes"},"repository":{"type":"Type","size":"Size","invalidjson":"Invalid JSON string","nofilesattached":"No files attached","filepicker":"File picker","logout":"Logout","nofilesavailable":"No files available","norepositoriesavailable":"Sorry, none of your current repositories can return files in the required format.","fileexistsdialogheader":"File exists","fileexistsdialog_editor":"A file with that name has already been attached to the text you are editing.","fileexistsdialog_filemanager":"A file with that name has already been attached","renameto":"Rename to \"{$a}\"","referencesexist":"There are {$a} alias\/shortcut files that use this file as their source"},"block":{"addtodock":"Move this to the dock","undockitem":"Undock this item","undockall":"Undock all","hidedockpanel":"Hide the dock panel","hidepanel":"Hide panel"},"langconfig":{"thisdirectionvertical":"btt"},"admin":{"confirmation":"Confirmation"}};
//]]>
</script>
<script type="text/javascript">
//<![CDATA[
YUI().use('node', function(Y) {
M.util.load_flowplayer();
setTimeout("fix_column_widths()", 20);
M.yui.galleryversion="2010.04.08-12-35";Y.use("node-menunav",function() {(function(){M.core_custom_menu.init(Y, "custom_menu_1");
})();
});
M.util.help_popups.setup(Y);
Y.on('domready', function() { M.util.init_maximised_embed(Y, "resourceobject"); });

});
//]]>
</script>
</body>
</html>