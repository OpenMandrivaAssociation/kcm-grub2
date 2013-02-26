# These macros are not present on the target distribution and are provided explicitly here
%define make_jobs %{__make} %{?_smp_mflags} VERBOSE=1

%define _kde4_configkcfgdir %{_kde4_sharedir}/config.kcfg

%define getres kcm-grub2-getres

Name:			kcm-grub2
Summary:		A KDE Control Module for configuring the GRUB2 bootloader
Version:		0.5.8
Release:		4
License:		GPLv3+
Url:			http://ksmanis.wordpress.com/projects/grub2-editor/
Group:			Graphical desktop/KDE
Source0:		%{name}-%{version}.tar.gz
Source1:		get_res.cpp
Source2:		%{name}.po
Patch0:			kcm-grub2-read-mode-from-file.patch
#%kde4_runtime_requires
Requires:		grub2
BuildRequires:	gcc-c++
BuildRequires:	kdelibs4-devel 
BuildRequires:	libhd-devel
BuildRequires:	pkgconfig(ImageMagick)

%description
Smoothly integrated in KDE System Settings, it is the central place 
for managing your GRUB2 configuration.

Author(s):
  Konstantinos Smanis <konstantinos.smanis@gmail.com>


%prep
%setup -q
cp -f %{SOURCE2} ./po/ru/kcm-grub2.po
%apply_patches
g++ %{SOURCE1} -l hd -o %{getres}

%build
#%cmake_kde4 -d ..
%cmake_kde4
cd .. && %make
#%make_jobs

%install
#%kde4_makeinstall -C build
#kde_post_install
#rm -fr %buildroot
make -C build DESTDIR=%buildroot install
%find_lang %{name}
install -d %{buildroot}%{_sbindir}
install -m 700 %{getres} %{buildroot}%{_sbindir}/%{getres}

%post
%{_sbindir}/%{getres}

%files -f %{name}.lang
%doc COPYING README
%{_datadir}/kde4/services/kcm_grub2.desktop
%{_kde_libdir}/kde4/kcm_grub2.so
%{_kde_libdir}/kde4/libexec/kcmgrub2helper
%config %{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmgrub2.conf
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmgrub2.service
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmgrub2.policy
%{_sbindir}/%{getres}


%changelog
* Fri Jul  27 2012 icedphoenix <icedphoenix@rosalab.ru>
+ Commit: 30b8df1
- graphical modes saved to file
  
  
