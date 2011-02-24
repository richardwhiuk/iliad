#ifndef ILIAD_FILE_PACKAGE
#define ILIAD_FILE_PACKAGE

#include <module.hpp>
#include <map>
#include <string>

namespace Iliad {

class Package {

public:
	Package(Server& server);
	virtual ~Package();

	virtual std::string name() = 0;
	virtual std::map<std::string, Iliad::Module* > modules() = 0;

};

}

#endif
