Summary:	Point-to-Point Tunneling Protocol (PPTP) Client
Summary(pl):	Klijent protoko³u PPTP
Name:		pptp-linux
Version:	1.4.0
Release:	0.1
License:	GPL
Provides:	pptp-linux
Requires:	ppp >= 2.4.2
Source0:	http://dl.sourceforge.net/pptpclient/%{name}-%{version}.tar.gz
Group:		Applications/System
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Client for the proprietary Microsoft Point-to-Point Tunneling
Protocol, PPTP. Allows connection to a PPTP based VPN as used by
employers and some cable and ADSL service providers. Requires MPPE
support in kernel.

%description -l pl


%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}{/ppp,/pptp.d}}
install pptp.8 $RPM_BUILD_ROOT%{_mandir}/man8/pptp.8
install pptp $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS INSTALL NEWS README TODO USING Documentation Reference
%attr(0755,root,root) %{_sbindir}/pptp
%attr(0444,root,root) %{_mandir}/man8/*
%attr(0755,root,root) %{_sysconfdir}/pptp.d
