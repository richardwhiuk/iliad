#include <server.hpp>
#include <core/loader.hpp>

Iliad::Server::Server(){

	Loader* core = new Core::Loader(*this);

	loaders[core->name()] = core;

}

Iliad::Server::~Server(){

	for(std::map<std::string, Loader*>::iterator it = loaders.begin(); it != loaders.end(); it ++){
		delete (it->second);
	}

}

void Iliad::Server::process(Iliad::Request& req, Iliad::Response& rep){

}


