#include <core/config/package.hpp>
#include <core/config/module.hpp>

Iliad::Core::Config::Package::Package(Iliad::Server& server) : Iliad::Package::Package(server), mServer(server) {
	
}

Iliad::Core::Config::Package::~Package(){

}

std::string Iliad::Core::Config::Package::name(){
	return "Config";
}

std::map<std::string, Iliad::Module*> Iliad::Core::Config::Package::modules(){
	std::map<std::string, Iliad::Module*> modules;

	Iliad::Module* module = new Iliad::Core::Config::Module(mServer);

	modules[module->name()] = module;

	return modules;
}

