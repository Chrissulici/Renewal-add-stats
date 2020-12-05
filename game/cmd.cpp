//search:
ACMD(do_user_horse_ride);

//add:
ACMD(do_stat_val);

//search:
	{	"\n",							NULL,							0,						POS_DEAD,			GM_IMPLEMENTOR	}

//add before:
	{	"stat_val",						do_stat_val,					0,						POS_DEAD,			GM_PLAYER	},