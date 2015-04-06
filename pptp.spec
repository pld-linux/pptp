Summary:	Point-to-Point Tunneling Protocol (PPTP) Client
Summary(pl.UTF-8):	Klient protokołu PPTP (Point-to-Point Tunneling Protocol)
Name:		pptp
Version:	1.8.0
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://downloads.sourceforge.net/pptpclient/%{name}-%{version}.tar.gz
# Source0-md5:	4efce9f263e2c3f38d79d9df222476de
Source1:	%{name}.tmpfiles
URL:		http://pptpclient.sourceforge.net/
Requires:	ppp >= 2.4.2
Provides:	pptp-linux
Obsoletes:	pptp-linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Client for the proprietary Microsoft Point-to-Point Tunneling
Protocol, PPTP. Allows connection to a PPTP based VPN as used by
employers and some cable and ADSL service providers. Requires MPPE
support in kernel.

%description -l pl.UTF-8
Klient PPTP - własnościowego protokołu Point-to-Point Tunneling
Microsoftu. Umożliwia łączenie z siecami VPN opartymi o PPTP używanymi
przez niektóre firmy oraz dostarczycieli łącz kablowych i ADSL. Wymaga
obsugi MPPE w jądrze.

%prep
%setup -q
%{__sed} -i -e 's/install -o root -m 555 pptp/install -m 755 pptp/' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	IP="/sbin/ip"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_localstatedir}/run/pptp \
	$RPM_BUILD_ROOT/usr/lib/tmpfiles.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO USING Documentation
%attr(755,root,root) %{_sbindir}/pptp
%attr(755,root,root) %{_sbindir}/pptpsetup
%{_mandir}/man8/pptp.8*
%{_mandir}/man8/pptpsetup.8*
/usr/lib/tmpfiles.d/%{name}.conf
%dir %attr(750,root,root) %{_localstatedir}/run/pptp
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ppp/options.pptp
