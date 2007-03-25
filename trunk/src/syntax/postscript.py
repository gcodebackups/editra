###############################################################################
#    Copyright (C) 2007 Cody Precord                                          #
#    cprecord@editra.org                                                      #
#                                                                             #
#    This program is free software; you can redistribute it and#or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation; either version 2 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program; if not, write to the                            #
#    Free Software Foundation, Inc.,                                          #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.                #
###############################################################################

"""
#-----------------------------------------------------------------------------#
# FILE: postscript.py                                                         #
# AUTHOR: Cody Precord                                                        #
#                                                                             #
# SUMMARY:                                                                    #
# Lexer configuration module for PostScript. (case sensitive)                 #
#                                                                             #
# TODO:                                                                       #
#                                                                             #
#-----------------------------------------------------------------------------#
"""

__revision__ = "$Id: Exp $"

#-----------------------------------------------------------------------------#

#---- Keyword Specifications ----#

# PS Level 1 Operators
ps_l1 = (0, "$error = == FontDirectory StandardEncoding UserObjects abs add "
            "aload anchorsearch and arc arcn arcto array ashow astore atan "
            "awidthshow begin bind bitshift bytesavailable cachestatus ceiling "
            "charpath clear cleardictstack cleartomark clip clippath closefile "
            "closepath concat concatmatrix copy copypage cos count countdictstack "
            "countexecstack counttomark currentcmykcolor currentcolorspace "
            "currentdash currentdict currentfile currentflat currentfont currentgray "
            "currenthsbcolor currentlinecap currentlinejoin currentlinewidth "
            "currentmatrix currentmiterlimit currentpagedevice currentpoint "
            "currentrgbcolor currentscreen currenttransfer cvi cvlit cvn cvr cvrs "
            "cvs cvx def defaultmatrix definefont dict dictstack div dtransform "
            "dup echo end eoclip eofill eq erasepage errordict exch exec execstack "
            "executeonly executive exit exp false file fill findfont flattenpath "
            "floor flush flushfile for forall ge get getinterval grestore "
            "grestoreall gsave gt idetmatrix idiv idtransform if ifelse image "
            "imagemask index initclip initgraphics initmatrix inustroke invertmatrix "
            "itransform known kshow le length lineto ln load log loop lt makefont "
            "mark matrix maxlength mod moveto mul ne neg newpath noaccess nor not "
            "null nulldevice or pathbbox pathforall pop print prompt pstack put "
            "putinterval quit rand rcheck rcurveto read readhexstring readline "
            "readonly readstring rectstroke repeat resetfile restore reversepath "
            "rlineto rmoveto roll rotate round rrand run save scale scalefont search "
            "setblackgeneration setcachedevice setcachelimit setcharwidth "
            "setcolorscreen setcolortransfer setdash setflat setfont setgray "
            "sethsbcolor setlinecap setlinejoin setlinewidth setmatrix setmiterlimit "
            "setpagedevice setrgbcolor setscreen settransfer setvmthreshold show "
            "showpage sin sqrt srand stack start status statusdict stop stopped "
            "store string stringwidth stroke strokepath sub systemdict token token "
            "transform translate true truncate type ueofill undefineresource "
            "userdict usertime version vmstatus wcheck where widthshow write "
            "writehexstring writestring xcheck xor")

# PS Level 2 Operators
ps_l2 = (1, "GlobalFontDirectory ISOLatin1Encoding SharedFontDirectory UserObject "
            "arct colorimage cshow currentblackgeneration currentcacheparams "
            "currentcmykcolor currentcolor currentcolorrendering currentcolorscreen "
            "currentcolorspace currentcolortransfer currentdevparams currentglobal "
            "currentgstate currenthalftone currentobjectformat currentoverprint "
            "currentpacking currentpagedevice currentshared currentstrokeadjust "
            "currentsystemparams currentundercolorremoval currentuserparams "
            "defineresource defineuserobject deletefile execform execuserobject "
            "filenameforall fileposition filter findencoding findresource gcheck "
            "globaldict glyphshow gstate ineofill infill instroke inueofill inufill "
            "inustroke languagelevel makepattern packedarray printobject product "
            "realtime rectclip rectfill rectstroke renamefile resourceforall "
            "resourcestatus revision rootfont scheck selectfont serialnumber "
            "setbbox setblackgeneration setcachedevice2 setcacheparams setcmykcolor "
            "setcolor setcolorrendering setcolorscreen setcolorspace setcolortranfer "
            "setdevparams setfileposition setglobal setgstate sethalftone "
            "setobjectformat setoverprint setpacking setpagedevice setpattern "
            "setshared setstrokeadjust setsystemparams setucacheparams "
            "setundercolorremoval setuserparams setvmthreshold shareddict startjob "
            "uappend ucache ucachestatus ueofill ufill undef undefinefont "
            "undefineresource undefineuserobject upath ustroke ustrokepath vmreclaim "
            "writeobject xshow xyshow yshow")

# PS Level 3 Operators
ps_l3 = (2, "cliprestore clipsave composefont currentsmoothness findcolorrendering "
            "setsmoothness shfill")

# RIP-specific operators Ghostscript
rip_op = (3, ".begintransparencygroup .begintransparencymask .bytestring .charboxpath "
             ".currentaccuratecurves .currentblendmode .currentcurvejoin "
             ".currentdashadapt .currentdotlength .currentfilladjust2 "
             ".currentlimitclamp .currentopacityalpha .currentoverprintmode "
             ".currentrasterop .currentshapealpha .currentsourcetransparent "
             ".currenttextknockout .currenttexturetransparent .dashpath .dicttomark "
             ".discardtransparencygroup .discardtransparencymask .endtransparencygroup "
             ".endtransparencymask .execn .filename .filename .fileposition .forceput "
             ".forceundef .forgetsave .getbitsrect .getdevice .inittransparencymask "
             ".knownget .locksafe .makeoperator .namestring .oserrno .oserrorstring "
             ".peekstring .rectappend .runandhide .setaccuratecurves .setblendmode "
             ".setcurvejoin .setdashadapt .setdebug .setdefaultmatrix .setdotlength "
             ".setfilladjust2 .setlimitclamp .setmaxlength .setopacityalpha "
             ".setoverprintmode .setrasterop .setsafe .setshapealpha "
             ".setsourcetransparent .settextknockout .settexturetransparent "
             ".stringbreak .stringmatch .tempfile .type1decrypt .type1encrypt "
             ".type1execchar .unread arccos arcsin copydevice copyscanlines "
             "currentdevice finddevice findlibfile findprotodevice flushpage "
             "getdeviceprops getenv makeimagedevice makewordimagedevice max min "
             "putdeviceprops setdevice")

# User Defined Operators
user_def = (4, "")

#---- Syntax Style Specs ----#
syntax_items = [ ('STC_PS_DEFAULT', 'default_style'),
                 ('STC_PS_BADSTRINGCHAR', 'unknown_style'),
                 ('STC_PS_BASE85STRING', 'string_style'),
                 ('STC_PS_COMMENT', 'comment_style'),
                 ('STC_PS_DSC_COMMENT', 'comment_style'),
                 ('STC_PS_DSC_VALUE', 'comment_style'), # STYLE ME
                 ('STC_PS_HEXSTRING', 'number_style'),
                 ('STC_PS_DSC_IMMEVAL', 'comment_style'), # STYLE ME
                 ('STC_PS_KEYWORD', 'class_style'),
                 ('STC_PS_LITERAL', 'scalar2_style'),
                 ('STC_PS_NAME', 'keyword_style'),
                 ('STC_PS_NUMBER', 'number_style'),
                 ('STC_PS_PAREN_ARRAY', 'default_style'), # STYLE ME
                 ('STC_PS_PAREN_DICT', 'default_style'), # STYLE ME
                 ('STC_OPS_PAREN_PROC', 'default_style'), # STYLE ME
                 ('STC_PS_TEXT', 'default_style') ]

#---- Extra Properties ----#
fold = ("fold", "1")
#-----------------------------------------------------------------------------#

#---- Required Module Functions ----#
def Keywords(type=0):
    """Returns Keyword Specifications List"""
    KEYWORDS = [ps_l1, ps_l2]
    return KEYWORDS

def SyntaxSpec(type=0):
    """Syntax Specifications"""
    return syntax_items

def Properties(type=0):
    """Properties"""
    return [ fold ]
#---- End Required Module Functions ----#

#---- Syntax Modules Internal Functions ----#
def KeywordString(option=0):
    """Returns the keyword string"""
    return None

#---- End Syntax Modules Internal Functions ----#

#-----------------------------------------------------------------------------#