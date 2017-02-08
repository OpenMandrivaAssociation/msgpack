%define major 2
%define libname %mklibname msgpack %{major}
%define devname %mklibname msgpack -d
%define staticname %mklibname msgpack -d -s

Name: msgpack
Version: 2.1.1
Release: 1
Source0: https://github.com/msgpack/msgpack-c/archive/cpp-%{version}.tar.gz
Summary: MessagePack implementation for C and C++
URL: http://msgpack.org/
License: Apache 2.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja

%description
MessagePack implementation for C and C++.

MessagePack is an efficient binary serialization format. It lets you exchange
data among multiple languages like JSON. But it's faster and smaller.
Small integers are encoded into a single byte, and typical short strings
require only one extra byte in addition to the strings themselves.

%package -n %{libname}
Summary: MessagePack implementation for C and C++
Group: System/Libraries

%description -n %{libname}
MessagePack implementation for C and C++.

MessagePack is an efficient binary serialization format. It lets you exchange
data among multiple languages like JSON. But it's faster and smaller.
Small integers are encoded into a single byte, and typical short strings
require only one extra byte in addition to the strings themselves.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

MessagePack implementation for C and C++.

MessagePack is an efficient binary serialization format. It lets you exchange
data among multiple languages like JSON. But it's faster and smaller.
Small integers are encoded into a single byte, and typical short strings
require only one extra byte in addition to the strings themselves.

%package -n %{staticname}
Summary: Static library for a MessagePack implementation for C and C++
Group: System/Libraries
Requires: %{devname} = %{EVRD}

%description -n %{staticname}
Static library for a MessagePack implementation for C and C++.

MessagePack is an efficient binary serialization format. It lets you exchange
data among multiple languages like JSON. But it's faster and smaller.
Small integers are encoded into a single byte, and typical short strings
require only one extra byte in addition to the strings themselves.

%prep
%setup -qn msgpack-c-cpp-%{version}
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files -n %{staticname}
%{_libdir}/*.a
