#ifndef ILIAD_FILE_MODULE
#define ILIAD_FILE_MODULE

#include <iliad.hpp>
#include <string>

namespace Iliad {

class Module {

public:
	Module(Iliad::Server& server);
	virtual ~Module();

	virtual std::string name() = 0;

};

}

#endif

