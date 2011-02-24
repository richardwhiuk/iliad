#include <iliad.hpp>
#include <module.hpp>

#include <string>

namespace Iliad {

namespace Core {

namespace Config {

class Module : public Iliad::Module {

public:

	Module(Iliad::Server& server);
	~Module();

	virtual std::string name();

};

}

}

}

