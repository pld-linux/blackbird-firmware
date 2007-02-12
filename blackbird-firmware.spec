#
# Conditional build:
%bcond_with     license_agreement       # generates package
#
Summary:	Firmware for the MPEG-2 encoding on cx23416 cards (cx88-blackbird)
Summary(pl.UTF-8):	Firmware dla kodera MPEG-2 na kartach z układem cx23416 (cx88-blackbird)
Name:		blackbird-firmware
Version:	2.05.032
%define         _rel    1
Release:	%{_rel}%{?with_license_agreement:wla}
License:	Publicly available but license unknown
Group:		System Environment/Kernel
######		Unknown group!
%if %{with license_agreement}
Source0:	ftp://ftp.hauppauge.com/Support/PVR250/beta/pvr150250350_inf.zip
# Source0-md5:	6582c050642b442e9a614c0cca5d41aa
%endif
URL:		http://ivtvdriver.org/index.php/Firmware
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the MPEG-2 encoder on the
cx23416 based TV tuner/PVR cards supported by cx88-blackbird driver.
%if !%{with license_agreement}
This package does not include the firmware. You should build the 
package yourself with "--with license_agreement" and install the wla 
release.
%endif

%description -l pl.UTF-8
Ten pakiet zawiera firmware sprzętowego kodera MPEG-2 obsługiwanych
przez sterownik cx88-blackbird kart telewizyjnych opartych ba układzie
cx23416.
%if !%{with license_agreement}
Ten pakiet nie zawiera firmware. Powinieneś zbudować pakiet własnoręcznie
z opcją "--with license_agreement" i zainstalować wersję wla.
%endif

%prep
%setup -q -c -T
%if %{with license_agreement}
unzip -q %{SOURCE0} HcwFalcn.rom
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

%if %{with license_agreement}
install HcwFalcn.rom $RPM_BUILD_ROOT/lib/firmware/blackbird-fw-enc.bin
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%if %{with license_agreement}
/lib/firmware/blackbird-fw-enc.bin
%endif
