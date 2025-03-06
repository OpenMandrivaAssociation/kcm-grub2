%define snap 20250306

Summary:	Plasma Systemsettings module for editing GRUB bootloader configuration
Name:		kcm-grub2
Version:	0.8.2%{?snap:~%{snap}}
Release:	1
License:	GPLv2
Group:		Graphical desktop/KDE
# KF5 port: https://github.com/maz-1/grub2-editor
Source0:	https://invent.kde.org/system/kcm-grub2/-/archive/work/nico/qt6/kcm-grub2-work-nico-qt6.tar.bz2
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(MagickCore)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Auth)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(packagekitqt6)
BuildRequires:	grub2 grub2-efi
BuildRequires:	grub2-extra
Requires:	grub2-extra
Requires:	grub2
Obsoletes:	grub2-editor <= 0.8.2-1
Provides:	grub2-editor <= 0.8.2-1

%description
A KDE Control Module for configuring the GRUB2 bootloader.
Unofficial KF6 port of the unofficial KF5 port.

%prep
%autosetup -p1 -n kcm-grub2-work-nico-qt6
%cmake \
	-G Ninja \
	-DGRUB_INSTALL_EXE="%{_sbindir}/grub2-install" \
	-DGRUB_MKCONFIG_EXE="%{_sbindir}/grub2-mkconfig" \
	-DGRUB_PROBE_EXE="%{_sbindir}/grub2-probe" \
	-DGRUB_SET_DEFAULT_EXE="%{_sbindir}/grub2-set-default" \
	-DGRUB_MAKE_PASSWD_EXE="%{_bindir}/grub2-mkpasswd-pbkdf2" \
	-DGRUB_MENU="/boot/grub2/grub.cfg" \
	-DGRUB_MENU_CUSTOM="/boot/grub2/custom.cfg" \
	-DGRUB_CONFIG="%{_sysconfdir}/default/grub" \
	-DGRUB_ENV="/boot/grub2/grubenv" \
	-DGRUB_MEMTEST="%{_sysconfdir}/grub.d/20_memtest86+" \
	-DGRUB_CONFIGDIR="%{_sysconfdir}/grub.d" \
	-DGRUB_SECURITY="01_header_passwd" \
	-DGRUB_RMECHO="99_rmecho" \
	|| cat CMakeFiles/CMakeOutput.log

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang kcm-grub2

%files -f kcm-grub2.lang
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmgrub2.service
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmgrub2.policy
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmgrub2.conf
%{_libdir}/libexec/kf6/kauth/kcmgrub2helper
%{_libdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_grub2.so
%{_datadir}/applications/kcm_grub2.desktop
