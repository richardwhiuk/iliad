#include <map>
#include <string>

#include <request.hpp>
#include <response.hpp>
#include <loader.hpp>
#include <package.hpp>
#include <module.hpp>

namespace Iliad {

class Server {

public:
	virtual ~Server();

	virtual void process(Iliad::Request& req, Iliad::Response& rep);

protected:
	Server();

private:

	std::map<std::string, Loader*> loaders;
	
	std::map<std::string, Package*> packages;

	std::map<std::string, Module*> modules;

};

}

