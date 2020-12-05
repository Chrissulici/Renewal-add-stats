#search:
		self.statusPlusCommandDict={
			"HTH" : "/stat ht",
			"INT" : "/stat iq",
			"STR" : "/stat st",
			"DEX" : "/stat dx",
		}

#change:
		self.statusPlusCommandDict={
			"HTH" : "/stat_val ht ",
			"INT" : "/stat_val iq ",
			"STR" : "/stat_val st ",
			"DEX" : "/stat_val dx ",
		}
		
#search:
	def __OnClickStatusPlusButton(self, statusKey):
		try:
			statusPlusCommand=self.statusPlusCommandDict[statusKey]
			net.SendChatPacket(statusPlusCommand)
		except KeyError, msg:
			dbg.TraceError("CharacterWindow.__OnClickStatusPlusButton KeyError: %s", msg)

#change:
	def __OnClickStatusPlusButton(self, statusKey):
		cmd = self.statusPlusCommandDict[statusKey]

		if app.IsPressed(app.DIK_LCONTROL):
			cmd = cmd + "10"
		else:
			cmd = cmd + "1"
			
		net.SendChatPacket(cmd)
		
#search:
	def __OverInStatButton(self, stat):
		try:
			self.__ShowStatToolTip(self.STAT_DESCRIPTION[stat])
		except KeyError:
			pass

#change:
	def __OverInStatButton(self, stat):	
		try:
			self.__ShowStatToolTip(self.STAT_DESCRIPTION[stat], localeInfo.EMOJI_CHARACTER_STATS_ADD, True)
		except KeyError:
			pass
			
#search:
	def __ShowStatToolTip(self, statDesc):
		self.toolTip.ClearToolTip()
		self.toolTip.AppendTextLine(statDesc)
		self.toolTip.Show()

#change:
	def __ShowStatToolTip(self, statDesc, statDesc2 = False, arg2 = False):
		self.toolTip.ClearToolTip()
		self.toolTip.AppendTextLine(statDesc)
		
		if arg2 == True:
			self.toolTip.AppendTextLine(statDesc2)
			
		self.toolTip.Show()
			
