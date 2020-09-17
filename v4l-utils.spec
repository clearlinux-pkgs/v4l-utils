#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x199A64FADFB500FF (gjasny@web.de)
#
Name     : v4l-utils
Version  : 1.20.0
Release  : 41
URL      : https://linuxtv.org/downloads/v4l-utils/v4l-utils-1.20.0.tar.bz2
Source0  : https://linuxtv.org/downloads/v4l-utils/v4l-utils-1.20.0.tar.bz2
Source1  : https://linuxtv.org/downloads/v4l-utils/v4l-utils-1.20.0.tar.bz2.asc
Summary  : Media controller library.
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: v4l-utils-bin = %{version}-%{release}
Requires: v4l-utils-config = %{version}-%{release}
Requires: v4l-utils-data = %{version}-%{release}
Requires: v4l-utils-lib = %{version}-%{release}
Requires: v4l-utils-license = %{version}-%{release}
Requires: v4l-utils-locales = %{version}-%{release}
Requires: v4l-utils-man = %{version}-%{release}
Requires: v4l-utils-services = %{version}-%{release}
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : doxygen
BuildRequires : graphviz
BuildRequires : libjpeg-turbo-dev
BuildRequires : llvm
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkgconfig(SDL2_image)
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glu)
BuildRequires : pkgconfig(libelf)
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
Requires: v4l-utils-data = %{version}-%{release}
Requires: v4l-utils-config = %{version}-%{release}
Requires: v4l-utils-license = %{version}-%{release}
Requires: v4l-utils-services = %{version}-%{release}

%description bin
bin components for the v4l-utils package.


%package config
Summary: config components for the v4l-utils package.
Group: Default

%description config
config components for the v4l-utils package.


%package data
Summary: data components for the v4l-utils package.
Group: Data

%description data
data components for the v4l-utils package.


%package dev
Summary: dev components for the v4l-utils package.
Group: Development
Requires: v4l-utils-lib = %{version}-%{release}
Requires: v4l-utils-bin = %{version}-%{release}
Requires: v4l-utils-data = %{version}-%{release}
Provides: v4l-utils-devel = %{version}-%{release}
Requires: v4l-utils = %{version}-%{release}

%description dev
dev components for the v4l-utils package.


%package extras
Summary: extras components for the v4l-utils package.
Group: Default

%description extras
extras components for the v4l-utils package.


%package extras-qt
Summary: extras-qt components for the v4l-utils package.
Group: Default

%description extras-qt
extras-qt components for the v4l-utils package.


%package lib
Summary: lib components for the v4l-utils package.
Group: Libraries
Requires: v4l-utils-data = %{version}-%{release}
Requires: v4l-utils-license = %{version}-%{release}

%description lib
lib components for the v4l-utils package.


%package license
Summary: license components for the v4l-utils package.
Group: Default

%description license
license components for the v4l-utils package.


%package locales
Summary: locales components for the v4l-utils package.
Group: Default

%description locales
locales components for the v4l-utils package.


%package man
Summary: man components for the v4l-utils package.
Group: Default

%description man
man components for the v4l-utils package.


%package services
Summary: services components for the v4l-utils package.
Group: Systemd services

%description services
services components for the v4l-utils package.


%prep
%setup -q -n v4l-utils-1.20.0
cd %{_builddir}/v4l-utils-1.20.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600307825
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1600307825
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/v4l-utils
cp %{_builddir}/v4l-utils-1.20.0/COPYING %{buildroot}/usr/share/package-licenses/v4l-utils/37d15fec7a725520bfff73f04485d0affc31dc51
cp %{_builddir}/v4l-utils-1.20.0/COPYING.libdvbv5 %{buildroot}/usr/share/package-licenses/v4l-utils/c8b571eca4828564399feba57f6e9f8f2f359858
cp %{_builddir}/v4l-utils-1.20.0/COPYING.libv4l %{buildroot}/usr/share/package-licenses/v4l-utils/bc667f27fc254baf99c2b974155ba528359ecc43
%make_install
%find_lang libdvbv5
%find_lang v4l-utils

%files
%defattr(-,root,root,-)
/usr/lib/udev/rc_keymaps/adstech_dvb_t_pci.toml
/usr/lib/udev/rc_keymaps/af9005.toml
/usr/lib/udev/rc_keymaps/alink_dtu_m.toml
/usr/lib/udev/rc_keymaps/allwinner_ba10_tv_box.toml
/usr/lib/udev/rc_keymaps/allwinner_i12_a20_tv_box.toml
/usr/lib/udev/rc_keymaps/anysee.toml
/usr/lib/udev/rc_keymaps/apac_viewcomp.toml
/usr/lib/udev/rc_keymaps/astrometa_t2hybrid.toml
/usr/lib/udev/rc_keymaps/asus_pc39.toml
/usr/lib/udev/rc_keymaps/asus_ps3_100.toml
/usr/lib/udev/rc_keymaps/ati_tv_wonder_hd_600.toml
/usr/lib/udev/rc_keymaps/ati_x10.toml
/usr/lib/udev/rc_keymaps/avermedia.toml
/usr/lib/udev/rc_keymaps/avermedia_a16d.toml
/usr/lib/udev/rc_keymaps/avermedia_cardbus.toml
/usr/lib/udev/rc_keymaps/avermedia_dvbt.toml
/usr/lib/udev/rc_keymaps/avermedia_m135a.toml
/usr/lib/udev/rc_keymaps/avermedia_m733a_rm_k6.toml
/usr/lib/udev/rc_keymaps/avermedia_rm_ks.toml
/usr/lib/udev/rc_keymaps/avertv_303.toml
/usr/lib/udev/rc_keymaps/az6027.toml
/usr/lib/udev/rc_keymaps/azurewave_ad_tu700.toml
/usr/lib/udev/rc_keymaps/beelink_gs1.toml
/usr/lib/udev/rc_keymaps/behold.toml
/usr/lib/udev/rc_keymaps/behold_columbus.toml
/usr/lib/udev/rc_keymaps/budget_ci_old.toml
/usr/lib/udev/rc_keymaps/cec.toml
/usr/lib/udev/rc_keymaps/cinergy.toml
/usr/lib/udev/rc_keymaps/cinergy_1400.toml
/usr/lib/udev/rc_keymaps/cinergyt2.toml
/usr/lib/udev/rc_keymaps/d680_dmb.toml
/usr/lib/udev/rc_keymaps/delock_61959.toml
/usr/lib/udev/rc_keymaps/dib0700_nec.toml
/usr/lib/udev/rc_keymaps/dib0700_rc5.toml
/usr/lib/udev/rc_keymaps/dibusb.toml
/usr/lib/udev/rc_keymaps/digitalnow_tinytwin.toml
/usr/lib/udev/rc_keymaps/digittrade.toml
/usr/lib/udev/rc_keymaps/digitv.toml
/usr/lib/udev/rc_keymaps/dish_network.toml
/usr/lib/udev/rc_keymaps/dm1105_nec.toml
/usr/lib/udev/rc_keymaps/dntv_live_dvb_t.toml
/usr/lib/udev/rc_keymaps/dntv_live_dvbt_pro.toml
/usr/lib/udev/rc_keymaps/dtt200u.toml
/usr/lib/udev/rc_keymaps/dvbsky.toml
/usr/lib/udev/rc_keymaps/dvico_mce.toml
/usr/lib/udev/rc_keymaps/dvico_portable.toml
/usr/lib/udev/rc_keymaps/em_terratec.toml
/usr/lib/udev/rc_keymaps/encore_enltv.toml
/usr/lib/udev/rc_keymaps/encore_enltv2.toml
/usr/lib/udev/rc_keymaps/encore_enltv_fm53.toml
/usr/lib/udev/rc_keymaps/evga_indtube.toml
/usr/lib/udev/rc_keymaps/eztv.toml
/usr/lib/udev/rc_keymaps/flydvb.toml
/usr/lib/udev/rc_keymaps/flyvideo.toml
/usr/lib/udev/rc_keymaps/fusionhdtv_mce.toml
/usr/lib/udev/rc_keymaps/gadmei_rm008z.toml
/usr/lib/udev/rc_keymaps/geekbox.toml
/usr/lib/udev/rc_keymaps/genius_tvgo_a11mce.toml
/usr/lib/udev/rc_keymaps/gotview7135.toml
/usr/lib/udev/rc_keymaps/haupp.toml
/usr/lib/udev/rc_keymaps/hauppauge.toml
/usr/lib/udev/rc_keymaps/hisi_poplar.toml
/usr/lib/udev/rc_keymaps/hisi_tv_demo.toml
/usr/lib/udev/rc_keymaps/imon_mce.toml
/usr/lib/udev/rc_keymaps/imon_pad.toml
/usr/lib/udev/rc_keymaps/imon_rsc.toml
/usr/lib/udev/rc_keymaps/iodata_bctv7e.toml
/usr/lib/udev/rc_keymaps/it913x_v1.toml
/usr/lib/udev/rc_keymaps/it913x_v2.toml
/usr/lib/udev/rc_keymaps/kaiomy.toml
/usr/lib/udev/rc_keymaps/khadas.toml
/usr/lib/udev/rc_keymaps/kii_pro.toml
/usr/lib/udev/rc_keymaps/kworld_315u.toml
/usr/lib/udev/rc_keymaps/kworld_pc150u.toml
/usr/lib/udev/rc_keymaps/kworld_plus_tv_analog.toml
/usr/lib/udev/rc_keymaps/leadtek_y04g0051.toml
/usr/lib/udev/rc_keymaps/lme2510.toml
/usr/lib/udev/rc_keymaps/manli.toml
/usr/lib/udev/rc_keymaps/mce_keyboard.toml
/usr/lib/udev/rc_keymaps/medion_x10.toml
/usr/lib/udev/rc_keymaps/medion_x10_digitainer.toml
/usr/lib/udev/rc_keymaps/medion_x10_or2x.toml
/usr/lib/udev/rc_keymaps/megasky.toml
/usr/lib/udev/rc_keymaps/msi_digivox_ii.toml
/usr/lib/udev/rc_keymaps/msi_digivox_iii.toml
/usr/lib/udev/rc_keymaps/msi_tvanywhere.toml
/usr/lib/udev/rc_keymaps/msi_tvanywhere_plus.toml
/usr/lib/udev/rc_keymaps/nebula.toml
/usr/lib/udev/rc_keymaps/nec_terratec_cinergy_xs.toml
/usr/lib/udev/rc_keymaps/norwood.toml
/usr/lib/udev/rc_keymaps/npgtech.toml
/usr/lib/udev/rc_keymaps/odroid.toml
/usr/lib/udev/rc_keymaps/opera1.toml
/usr/lib/udev/rc_keymaps/pctv_sedna.toml
/usr/lib/udev/rc_keymaps/pinnacle310e.toml
/usr/lib/udev/rc_keymaps/pinnacle_color.toml
/usr/lib/udev/rc_keymaps/pinnacle_grey.toml
/usr/lib/udev/rc_keymaps/pinnacle_pctv_hd.toml
/usr/lib/udev/rc_keymaps/pixelview.toml
/usr/lib/udev/rc_keymaps/pixelview_002t.toml
/usr/lib/udev/rc_keymaps/pixelview_mk12.toml
/usr/lib/udev/rc_keymaps/pixelview_new.toml
/usr/lib/udev/rc_keymaps/powercolor_real_angel.toml
/usr/lib/udev/rc_keymaps/proteus_2309.toml
/usr/lib/udev/rc_keymaps/protocols/grundig.o
/usr/lib/udev/rc_keymaps/protocols/imon_rsc.o
/usr/lib/udev/rc_keymaps/protocols/manchester.o
/usr/lib/udev/rc_keymaps/protocols/pulse_distance.o
/usr/lib/udev/rc_keymaps/protocols/pulse_length.o
/usr/lib/udev/rc_keymaps/protocols/raw.o
/usr/lib/udev/rc_keymaps/protocols/rc_mm.o
/usr/lib/udev/rc_keymaps/protocols/samsung36.o
/usr/lib/udev/rc_keymaps/protocols/xbox-dvd.o
/usr/lib/udev/rc_keymaps/purpletv.toml
/usr/lib/udev/rc_keymaps/pv951.toml
/usr/lib/udev/rc_keymaps/rc6_mce.toml
/usr/lib/udev/rc_keymaps/real_audio_220_32_keys.toml
/usr/lib/udev/rc_keymaps/reddo.toml
/usr/lib/udev/rc_keymaps/snapstream_firefly.toml
/usr/lib/udev/rc_keymaps/streamzap.toml
/usr/lib/udev/rc_keymaps/su3000.toml
/usr/lib/udev/rc_keymaps/tango.toml
/usr/lib/udev/rc_keymaps/tanix_tx3mini.toml
/usr/lib/udev/rc_keymaps/tanix_tx5max.toml
/usr/lib/udev/rc_keymaps/tbs_nec.toml
/usr/lib/udev/rc_keymaps/technisat_ts35.toml
/usr/lib/udev/rc_keymaps/technisat_usb2.toml
/usr/lib/udev/rc_keymaps/terratec_cinergy_c_pci.toml
/usr/lib/udev/rc_keymaps/terratec_cinergy_s2_hd.toml
/usr/lib/udev/rc_keymaps/terratec_cinergy_xs.toml
/usr/lib/udev/rc_keymaps/terratec_slim.toml
/usr/lib/udev/rc_keymaps/terratec_slim_2.toml
/usr/lib/udev/rc_keymaps/tevii_nec.toml
/usr/lib/udev/rc_keymaps/tivo.toml
/usr/lib/udev/rc_keymaps/total_media_in_hand.toml
/usr/lib/udev/rc_keymaps/total_media_in_hand_02.toml
/usr/lib/udev/rc_keymaps/trekstor.toml
/usr/lib/udev/rc_keymaps/tt_1500.toml
/usr/lib/udev/rc_keymaps/tvwalkertwin.toml
/usr/lib/udev/rc_keymaps/twinhan_dtv_cab_ci.toml
/usr/lib/udev/rc_keymaps/twinhan_vp1027_dvbs.toml
/usr/lib/udev/rc_keymaps/vega_s9x.toml
/usr/lib/udev/rc_keymaps/videomate_k100.toml
/usr/lib/udev/rc_keymaps/videomate_s350.toml
/usr/lib/udev/rc_keymaps/videomate_tv_pvr.toml
/usr/lib/udev/rc_keymaps/vp702x.toml
/usr/lib/udev/rc_keymaps/wetek_hub.toml
/usr/lib/udev/rc_keymaps/wetek_play2.toml
/usr/lib/udev/rc_keymaps/winfast.toml
/usr/lib/udev/rc_keymaps/winfast_usbii_deluxe.toml
/usr/lib/udev/rc_keymaps/wobo_i5.toml
/usr/lib/udev/rc_keymaps/x96max.toml
/usr/lib/udev/rc_keymaps/xbox_dvd.toml
/usr/lib/udev/rc_keymaps/zx_irdec.toml

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

%files data
%defattr(-,root,root,-)
/usr/share/applications/qv4l2.desktop
/usr/share/applications/qvidcap.desktop
/usr/share/icons/hicolor/16x16/apps/qv4l2.png
/usr/share/icons/hicolor/16x16/apps/qvidcap.png
/usr/share/icons/hicolor/24x24/apps/qv4l2.png
/usr/share/icons/hicolor/24x24/apps/qvidcap.png
/usr/share/icons/hicolor/32x32/apps/qv4l2.png
/usr/share/icons/hicolor/32x32/apps/qvidcap.png
/usr/share/icons/hicolor/64x64/apps/qv4l2.png
/usr/share/icons/hicolor/64x64/apps/qvidcap.png
/usr/share/icons/hicolor/scalable/apps/qv4l2.svg
/usr/share/icons/hicolor/scalable/apps/qvidcap.svg

%files dev
%defattr(-,root,root,-)
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
/usr/include/libv4l-plugin.h
/usr/include/libv4l1-videodev.h
/usr/include/libv4l1.h
/usr/include/libv4l2.h
/usr/include/libv4l2rds.h
/usr/include/libv4lconvert.h
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

%files extras
%defattr(-,root,root,-)
/usr/lib64/libv4l/ov511-decomp
/usr/lib64/libv4l/ov518-decomp

%files extras-qt
%defattr(-,root,root,-)
/usr/bin/qv4l2
/usr/bin/qvidcap

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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/v4l-utils/37d15fec7a725520bfff73f04485d0affc31dc51
/usr/share/package-licenses/v4l-utils/bc667f27fc254baf99c2b974155ba528359ecc43
/usr/share/package-licenses/v4l-utils/c8b571eca4828564399feba57f6e9f8f2f359858

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cec-compliance.1
/usr/share/man/man1/cec-ctl.1
/usr/share/man/man1/cec-follower.1
/usr/share/man/man1/dvb-fe-tool.1
/usr/share/man/man1/dvb-format-convert.1
/usr/share/man/man1/dvbv5-scan.1
/usr/share/man/man1/dvbv5-zap.1
/usr/share/man/man1/ir-ctl.1
/usr/share/man/man1/ir-keytable.1
/usr/share/man/man1/qv4l2.1
/usr/share/man/man1/qvidcap.1
/usr/share/man/man1/v4l2-compliance.1
/usr/share/man/man1/v4l2-ctl.1
/usr/share/man/man5/rc_keymap.5

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/systemd-udevd.service.d/50-rc_keymap.conf

%files locales -f libdvbv5.lang -f v4l-utils.lang
%defattr(-,root,root,-)

