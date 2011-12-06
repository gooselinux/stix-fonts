%global fontname stix
%global fontconf 61-%{fontname}

%global archivename STIXBeta

%global common_desc \
The mission of the Scientific and Technical Information Exchange (STIX) font \
creation project is the preparation of a comprehensive set of fonts that serve \
the scientific and engineering community in the process from manuscript \
creation through final publication, both in electronic and print formats.

Name:    %{fontname}-fonts
Version: 0.9
Release: 13.1%{?dist}
Summary: STIX scientific and engineering fonts

Group:     User Interface/X
License:   STIX
URL:       http://www.stixfonts.org/
Source0:   %{archivename}.zip
Source1:   %{name}-License.txt
Source2:   stix-fonts-fontconfig.conf
Source3:   stix-fonts-pua-fontconfig.conf
Source4:   stix-fonts-integrals-fontconfig.conf
Source5:   stix-fonts-sizes-fontconfig.conf
Source6:   stix-fonts-variants-fontconfig.conf
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
%common_desc

This package includes base Unicode fonts containing most glyphs for standard
use.


%package -n %{fontname}-pua-fonts
Group:     User Interface/X
Summary:  STIX scientific and engineering fonts, PUA glyphs
Requires: %{name} = %{version}-%{release}

Obsoletes: %{name}-pua < 0.9-10

%description -n %{fontname}-pua-fonts
%common_desc

This package includes fonts containing glyphs called out from the Unicode
Private Use Area (PUA) range. Glyphs in this range do not have an official
Unicode codepoint. They're generally accessible only through specialised
software. Text using them will break if they're ever accepted by the Unicode
Consortium and moved to an official codepoint.

%_font_pkg -n pua -f %{fontconf}-pua.conf STIXNonUni*otf


%package -n %{fontname}-integrals-fonts
Group:     User Interface/X
Summary:  STIX scientific and engineering fonts, additional integral glyphs
Requires: %{name} = %{version}-%{release}

Obsoletes: %{name}-integrals < 0.9-10

%description -n %{fontname}-integrals-fonts
%common_desc

This package includes fonts containing additional integrals of various size
and slant.

%_font_pkg -n integrals -f %{fontconf}-integrals.conf STIXInt*.otf


%package -n %{fontname}-sizes-fonts
Group:     User Interface/X
Summary:  STIX scientific and engineering fonts, additional glyph sizes
Requires: %{name} = %{version}-%{release}

Obsoletes: %{name}-sizes < 0.9-10

%description -n %{fontname}-sizes-fonts
%common_desc

This package includes fonts containing glyphs in additional sizes (Mostly
"fence" and "piece" glyphs).

%_font_pkg -n sizes -f %{fontconf}-sizes.conf STIXSiz*.otf


%package -n %{fontname}-variants-fonts
Group:     User Interface/X
Summary:  STIX scientific and engineering fonts, additional glyph variants
Requires: %{name} = %{version}-%{release}

Obsoletes: %{name}-variants < 0.9-10

%description -n %{fontname}-variants-fonts
%common_desc

This package includes fonts containing alternative variants of some glyphs.

%_font_pkg -n variants -f %{fontconf}-variants.conf STIXVar*otf


%prep
%setup -c -q -n %{archivename}
install -m 0644 -p %{SOURCE1} License.txt
for txt in *.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pua.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-integrals.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sizes.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-variants.conf

for fconf in %{fontconf}.conf \
             %{fontconf}-pua.conf \
             %{fontconf}-integrals.conf \
             %{fontconf}-sizes.conf \
             %{fontconf}-variants.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done


%clean
rm -fr %{buildroot}


%_font_pkg -f %{fontconf}.conf STIXGeneral*otf

%doc *.txt


%changelog
* Tue Dec 08 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.9-13.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.9-11
— prepare for F11 mass rebuild, new rpm and new fontpackages

* Fri Jan 16 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.9-10
‣ Convert to new naming guidelines

* Sun Nov 23 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.9-9
ᛤ ‘rpm-fonts’ renamed to “fontpackages”

* Fri Nov 14 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.9-8
▤ Rebuild using new « rpm-fonts »

* Fri Jul 11 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.9-7
⌖ Fedora 10 alpha general package cleanup

* Thu Nov 1 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☺ 0.9-6
 ✓ Add some fontconfig aliasing rules
☢ 0.9-4
⚠ Initial experimental packaging
