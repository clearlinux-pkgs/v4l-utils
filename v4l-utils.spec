#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x199A64FADFB500FF (gjasny@web.de)
#
Name     : v4l-utils
Version  : 1.14.2
Release  : 12
URL      : https://linuxtv.org/downloads/v4l-utils/v4l-utils-1.14.2.tar.bz2
Source0  : https://linuxtv.org/downloads/v4l-utils/v4l-utils-1.14.2.tar.bz2
Source99 : https://linuxtv.org/downloads/v4l-utils/v4l-utils-1.14.2.tar.bz2.asc
Summary  : Media controller library.
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: v4l-utils-bin
Requires: v4l-utils-config
Requires: v4l-utils-lib
Requires: v4l-utils-locales
Requires: v4l-utils-doc
BuildRequires : doxygen
BuildRequires : graphviz
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(SDL2_image)
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glu)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(sdl2)
BuildRequires : pkgconfig(x11)

%description
v4l-utils
---------
Linux utilities and libraries to handle media devices (TV devices,
capture devices, radio devices, remote controllers).

%package bin
Summary: bin components for the v4l-utils package.
Group: Binaries
Requires: v4l-utils-config

%description bin
bin components for the v4l-utils package.


%package config
Summary: config components for the v4l-utils package.
Group: Default

%description config
config components for the v4l-utils package.


%package dev
Summary: dev components for the v4l-utils package.
Group: Development
Requires: v4l-utils-lib
Requires: v4l-utils-bin
Provides: v4l-utils-devel

%description dev
dev components for the v4l-utils package.


%package doc
Summary: doc components for the v4l-utils package.
Group: Documentation

%description doc
doc components for the v4l-utils package.


%package lib
Summary: lib components for the v4l-utils package.
Group: Libraries

%description lib
lib components for the v4l-utils package.


%package locales
Summary: locales components for the v4l-utils package.
Group: Default

%description locales
locales components for the v4l-utils package.


%prep
%setup -q -n v4l-utils-1.14.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1518269403
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1518269403
rm -rf %{buildroot}
%make_install
%find_lang libdvbv5
%find_lang v4l-utils

%files
%defattr(-,root,root,-)
/usr/lib/udev/rc_keymaps/adstech_dvb_t_pci
/usr/lib/udev/rc_keymaps/af9005
/usr/lib/udev/rc_keymaps/alink_dtu_m
/usr/lib/udev/rc_keymaps/allwinner_ba10_tv_box
/usr/lib/udev/rc_keymaps/allwinner_i12_a20_tv_box
/usr/lib/udev/rc_keymaps/anysee
/usr/lib/udev/rc_keymaps/apac_viewcomp
/usr/lib/udev/rc_keymaps/astrometa_t2hybrid
/usr/lib/udev/rc_keymaps/asus_pc39
/usr/lib/udev/rc_keymaps/asus_ps3_100
/usr/lib/udev/rc_keymaps/ati_tv_wonder_hd_600
/usr/lib/udev/rc_keymaps/ati_x10
/usr/lib/udev/rc_keymaps/avermedia
/usr/lib/udev/rc_keymaps/avermedia_a16d
/usr/lib/udev/rc_keymaps/avermedia_cardbus
/usr/lib/udev/rc_keymaps/avermedia_dvbt
/usr/lib/udev/rc_keymaps/avermedia_m135a
/usr/lib/udev/rc_keymaps/avermedia_m733a_rm_k6
/usr/lib/udev/rc_keymaps/avermedia_rm_ks
/usr/lib/udev/rc_keymaps/avertv_303
/usr/lib/udev/rc_keymaps/az6027
/usr/lib/udev/rc_keymaps/azurewave_ad_tu700
/usr/lib/udev/rc_keymaps/behold
/usr/lib/udev/rc_keymaps/behold_columbus
/usr/lib/udev/rc_keymaps/budget_ci_old
/usr/lib/udev/rc_keymaps/cec
/usr/lib/udev/rc_keymaps/cinergy
/usr/lib/udev/rc_keymaps/cinergy_1400
/usr/lib/udev/rc_keymaps/cinergyt2
/usr/lib/udev/rc_keymaps/d680_dmb
/usr/lib/udev/rc_keymaps/delock_61959
/usr/lib/udev/rc_keymaps/dib0700_nec
/usr/lib/udev/rc_keymaps/dib0700_rc5
/usr/lib/udev/rc_keymaps/dibusb
/usr/lib/udev/rc_keymaps/digitalnow_tinytwin
/usr/lib/udev/rc_keymaps/digittrade
/usr/lib/udev/rc_keymaps/digitv
/usr/lib/udev/rc_keymaps/dm1105_nec
/usr/lib/udev/rc_keymaps/dntv_live_dvb_t
/usr/lib/udev/rc_keymaps/dntv_live_dvbt_pro
/usr/lib/udev/rc_keymaps/dtt200u
/usr/lib/udev/rc_keymaps/dvbsky
/usr/lib/udev/rc_keymaps/dvico_mce
/usr/lib/udev/rc_keymaps/dvico_portable
/usr/lib/udev/rc_keymaps/em_terratec
/usr/lib/udev/rc_keymaps/encore_enltv
/usr/lib/udev/rc_keymaps/encore_enltv2
/usr/lib/udev/rc_keymaps/encore_enltv_fm53
/usr/lib/udev/rc_keymaps/evga_indtube
/usr/lib/udev/rc_keymaps/eztv
/usr/lib/udev/rc_keymaps/flydvb
/usr/lib/udev/rc_keymaps/flyvideo
/usr/lib/udev/rc_keymaps/fusionhdtv_mce
/usr/lib/udev/rc_keymaps/gadmei_rm008z
/usr/lib/udev/rc_keymaps/geekbox
/usr/lib/udev/rc_keymaps/genius_tvgo_a11mce
/usr/lib/udev/rc_keymaps/gotview7135
/usr/lib/udev/rc_keymaps/haupp
/usr/lib/udev/rc_keymaps/hauppauge
/usr/lib/udev/rc_keymaps/hisi_poplar
/usr/lib/udev/rc_keymaps/hisi_tv_demo
/usr/lib/udev/rc_keymaps/imon_mce
/usr/lib/udev/rc_keymaps/imon_pad
/usr/lib/udev/rc_keymaps/iodata_bctv7e
/usr/lib/udev/rc_keymaps/it913x_v1
/usr/lib/udev/rc_keymaps/it913x_v2
/usr/lib/udev/rc_keymaps/kaiomy
/usr/lib/udev/rc_keymaps/kworld_315u
/usr/lib/udev/rc_keymaps/kworld_pc150u
/usr/lib/udev/rc_keymaps/kworld_plus_tv_analog
/usr/lib/udev/rc_keymaps/leadtek_y04g0051
/usr/lib/udev/rc_keymaps/lme2510
/usr/lib/udev/rc_keymaps/manli
/usr/lib/udev/rc_keymaps/medion_x10
/usr/lib/udev/rc_keymaps/medion_x10_digitainer
/usr/lib/udev/rc_keymaps/medion_x10_or2x
/usr/lib/udev/rc_keymaps/megasky
/usr/lib/udev/rc_keymaps/msi_digivox_ii
/usr/lib/udev/rc_keymaps/msi_digivox_iii
/usr/lib/udev/rc_keymaps/msi_tvanywhere
/usr/lib/udev/rc_keymaps/msi_tvanywhere_plus
/usr/lib/udev/rc_keymaps/nebula
/usr/lib/udev/rc_keymaps/nec_terratec_cinergy_xs
/usr/lib/udev/rc_keymaps/norwood
/usr/lib/udev/rc_keymaps/npgtech
/usr/lib/udev/rc_keymaps/opera1
/usr/lib/udev/rc_keymaps/pctv_sedna
/usr/lib/udev/rc_keymaps/pinnacle310e
/usr/lib/udev/rc_keymaps/pinnacle_color
/usr/lib/udev/rc_keymaps/pinnacle_grey
/usr/lib/udev/rc_keymaps/pinnacle_pctv_hd
/usr/lib/udev/rc_keymaps/pixelview
/usr/lib/udev/rc_keymaps/pixelview_002t
/usr/lib/udev/rc_keymaps/pixelview_mk12
/usr/lib/udev/rc_keymaps/pixelview_new
/usr/lib/udev/rc_keymaps/powercolor_real_angel
/usr/lib/udev/rc_keymaps/proteus_2309
/usr/lib/udev/rc_keymaps/purpletv
/usr/lib/udev/rc_keymaps/pv951
/usr/lib/udev/rc_keymaps/rc6_mce
/usr/lib/udev/rc_keymaps/real_audio_220_32_keys
/usr/lib/udev/rc_keymaps/reddo
/usr/lib/udev/rc_keymaps/snapstream_firefly
/usr/lib/udev/rc_keymaps/streamzap
/usr/lib/udev/rc_keymaps/su3000
/usr/lib/udev/rc_keymaps/tango
/usr/lib/udev/rc_keymaps/tbs_nec
/usr/lib/udev/rc_keymaps/technisat_ts35
/usr/lib/udev/rc_keymaps/technisat_usb2
/usr/lib/udev/rc_keymaps/terratec_cinergy_c_pci
/usr/lib/udev/rc_keymaps/terratec_cinergy_s2_hd
/usr/lib/udev/rc_keymaps/terratec_cinergy_xs
/usr/lib/udev/rc_keymaps/terratec_slim
/usr/lib/udev/rc_keymaps/terratec_slim_2
/usr/lib/udev/rc_keymaps/tevii_nec
/usr/lib/udev/rc_keymaps/tivo
/usr/lib/udev/rc_keymaps/total_media_in_hand
/usr/lib/udev/rc_keymaps/total_media_in_hand_02
/usr/lib/udev/rc_keymaps/trekstor
/usr/lib/udev/rc_keymaps/tt_1500
/usr/lib/udev/rc_keymaps/tvwalkertwin
/usr/lib/udev/rc_keymaps/twinhan_dtv_cab_ci
/usr/lib/udev/rc_keymaps/twinhan_vp1027_dvbs
/usr/lib/udev/rc_keymaps/videomate_k100
/usr/lib/udev/rc_keymaps/videomate_s350
/usr/lib/udev/rc_keymaps/videomate_tv_pvr
/usr/lib/udev/rc_keymaps/vp702x
/usr/lib/udev/rc_keymaps/winfast
/usr/lib/udev/rc_keymaps/winfast_usbii_deluxe
/usr/lib/udev/rc_keymaps/wobo_i5
/usr/lib/udev/rc_keymaps/zx_irdec
/usr/lib64/libv4l/ov511-decomp
/usr/lib64/libv4l/ov518-decomp

%files bin
%defattr(-,root,root,-)
/usr/bin/cec-compliance
/usr/bin/cec-ctl
/usr/bin/cec-follower
/usr/bin/cx18-ctl
/usr/bin/decode_tm6000
/usr/bin/dvb-fe-tool
/usr/bin/dvb-format-convert
/usr/bin/dvbv5-daemon
/usr/bin/dvbv5-scan
/usr/bin/dvbv5-zap
/usr/bin/ir-ctl
/usr/bin/ir-keytable
/usr/bin/ivtv-ctl
/usr/bin/media-ctl
/usr/bin/rds-ctl
/usr/bin/v4l2-compliance
/usr/bin/v4l2-ctl
/usr/bin/v4l2-dbg
/usr/bin/v4l2-sysfs-path

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/70-infrared.rules

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/libdvbv5/atsc_eit.h
/usr/include/libdvbv5/atsc_header.h
/usr/include/libdvbv5/cat.h
/usr/include/libdvbv5/countries.h
/usr/include/libdvbv5/crc32.h
/usr/include/libdvbv5/desc_atsc_service_location.h
/usr/include/libdvbv5/desc_ca.h
/usr/include/libdvbv5/desc_ca_identifier.h
/usr/include/libdvbv5/desc_cable_delivery.h
/usr/include/libdvbv5/desc_event_extended.h
/usr/include/libdvbv5/desc_event_short.h
/usr/include/libdvbv5/desc_extension.h
/usr/include/libdvbv5/desc_frequency_list.h
/usr/include/libdvbv5/desc_hierarchy.h
/usr/include/libdvbv5/desc_isdbt_delivery.h
/usr/include/libdvbv5/desc_language.h
/usr/include/libdvbv5/desc_logical_channel.h
/usr/include/libdvbv5/desc_network_name.h
/usr/include/libdvbv5/desc_partial_reception.h
/usr/include/libdvbv5/desc_sat.h
/usr/include/libdvbv5/desc_service.h
/usr/include/libdvbv5/desc_t2_delivery.h
/usr/include/libdvbv5/desc_terrestrial_delivery.h
/usr/include/libdvbv5/desc_ts_info.h
/usr/include/libdvbv5/descriptors.h
/usr/include/libdvbv5/dvb-demux.h
/usr/include/libdvbv5/dvb-dev.h
/usr/include/libdvbv5/dvb-fe.h
/usr/include/libdvbv5/dvb-file.h
/usr/include/libdvbv5/dvb-frontend.h
/usr/include/libdvbv5/dvb-log.h
/usr/include/libdvbv5/dvb-sat.h
/usr/include/libdvbv5/dvb-scan.h
/usr/include/libdvbv5/dvb-v5-std.h
/usr/include/libdvbv5/eit.h
/usr/include/libdvbv5/header.h
/usr/include/libdvbv5/libdvb-version.h
/usr/include/libdvbv5/mgt.h
/usr/include/libdvbv5/mpeg_es.h
/usr/include/libdvbv5/mpeg_pes.h
/usr/include/libdvbv5/mpeg_ts.h
/usr/include/libdvbv5/nit.h
/usr/include/libdvbv5/pat.h
/usr/include/libdvbv5/pmt.h
/usr/include/libdvbv5/sdt.h
/usr/include/libdvbv5/vct.h
/usr/lib64/libdvbv5.so
/usr/lib64/libv4l1.so
/usr/lib64/libv4l2.so
/usr/lib64/libv4l2rds.so
/usr/lib64/libv4lconvert.so
/usr/lib64/pkgconfig/libdvbv5.pc
/usr/lib64/pkgconfig/libv4l1.pc
/usr/lib64/pkgconfig/libv4l2.pc
/usr/lib64/pkgconfig/libv4l2rds.pc
/usr/lib64/pkgconfig/libv4lconvert.pc
/usr/lib64/v4l1compat.so
/usr/lib64/v4l2convert.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdvbv5.so.0
/usr/lib64/libdvbv5.so.0.0.0
/usr/lib64/libv4l/plugins/libv4l-mplane.so
/usr/lib64/libv4l/v4l1compat.so
/usr/lib64/libv4l/v4l2convert.so
/usr/lib64/libv4l1.so.0
/usr/lib64/libv4l1.so.0.0.0
/usr/lib64/libv4l2.so.0
/usr/lib64/libv4l2.so.0.0.0
/usr/lib64/libv4l2rds.so.0
/usr/lib64/libv4l2rds.so.0.0.0
/usr/lib64/libv4lconvert.so.0
/usr/lib64/libv4lconvert.so.0.0.0

%files locales -f libdvbv5.lang -f v4l-utils.lang
%defattr(-,root,root,-)

