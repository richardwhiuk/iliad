#include <iliad.hpp>
#include <package.hpp>
#include <core/config/package.hpp>
#include <core/loader.hpp>

Iliad::Core::Loader::Loader(Iliad::Server& server) : Iliad::Loader(server), mServer(server) {

}

Iliad::Core::Loader::~Loader(){

}

std::string Iliad::Core::Loader::name(){
	return "Core";
}

std::map<std::string, Iliad::Package*> Iliad::Core::Loader::packages(){
	std::map<std::string, Iliad::Package*> packages;
	
	Iliad::Package* config = new Iliad::Core::Config::Package(mServer);

	packages[config->name()] = config;
	
	return packages;
}

