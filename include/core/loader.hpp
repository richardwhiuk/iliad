#include <loader.hpp>

namespace Iliad {

namespace Core {

class Loader : public Iliad::Loader {

public:

	Loader(Iliad::Server& server);
	virtual ~Loader();
	virtual std::map<std::string, Iliad::Package*> packages();
	virtual std::string name();

private:

	Iliad::Server& mServer;

};

}

}

