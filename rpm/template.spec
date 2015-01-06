Name:           ros-indigo-turtlebot-bringup
Version:        2.3.4
Release:        0%{?dist}
Summary:        ROS turtlebot_bringup package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/turtlebot_bringup
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-create-node
Requires:       ros-indigo-depthimage-to-laserscan
Requires:       ros-indigo-diagnostic-aggregator
Requires:       ros-indigo-kobuki-bumper2pc
Requires:       ros-indigo-kobuki-capabilities
Requires:       ros-indigo-kobuki-node
Requires:       ros-indigo-kobuki-safety-controller
Requires:       ros-indigo-laptop-battery-monitor
Requires:       ros-indigo-openni-launch
Requires:       ros-indigo-robot-pose-ekf
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-rocon-app-manager
Requires:       ros-indigo-turtlebot-description
Requires:       ros-indigo-yocs-cmd-vel-mux
Requires:       ros-indigo-zeroconf-avahi
BuildRequires:  ros-indigo-catkin

%description
turtlebot_bringup provides roslaunch scripts for starting the TurtleBot base
functionality.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jan 07 2015 Daniel Stonier <d.stonier@gmail.com> - 2.3.4-0
- Autogenerated by Bloom

* Mon Jan 05 2015 Daniel Stonier <d.stonier@gmail.com> - 2.3.3-0
- Autogenerated by Bloom

* Tue Dec 30 2014 Daniel Stonier <d.stonier@gmail.com> - 2.3.2-0
- Autogenerated by Bloom

