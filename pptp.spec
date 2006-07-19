Summary:	Point-to-Point Tunneling Protocol (PPTP) Client
Summary(pl):	Klient protoko³u PPTP (Point-to-Point Tunneling Protocol)
Name:		pptp
Version:	1.7.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/pptpclient/%{name}-%{version}.tar.gz
# Source0-md5:	b47735ba5d6d37dfdbccb85afc044ede
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

%description -l pl
Klient PPTP - w³asno¶ciowego protoko³u Point-to-Point Tunneling
Microsoftu. Umo¿liwia ³±czenie z siecami VPN opartymi o PPTP u¿ywanymi
przez niektóre firmy oraz dostarczycieli ³±cz kablowych i ADSL. Wymaga
obsugi MPPE w j±drze.

%prep
%setup -q
%{__sed} -i -e 's/install -o root -m 555 pptp/install -m 755 pptp/' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_localstatedir}/run/pptp

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO USING Documentation Reference
%attr(755,root,root) %{_sbindir}/pptp
%{_mandir}/man8/pptp.8*
%dir %attr(750,root,root) %{_localstatedir}/run/pptp
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ppp/options.pptp
