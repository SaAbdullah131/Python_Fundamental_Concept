function scrapeCommentsWithReplies(){
  var sheet = SpreadsheetApp.getActiveSpreadsheet();
  var result = [['Channel URL', 'Name','Comment','Time','Likes','Reply Count','Reply Author','Reply','Published','Updated']];
  var vid = sheet.getSheetByName('Input').getRange(1,2).getValue();
  var nextPageToken = undefined;
  
  while(true){
      var commentThreads = YouTube.CommentThreads.list('snippet', {videoId: vid, maxResults: 100, pageToken: nextPageToken})
      nextPageToken = commentThreads.nextPageToken
      for (var row = 0; row<commentThreads.items.length; row++) {
            result.push([
                //commentThreads.items[row].snippet.topLevelComment.snippet.authorChannelUrl,
                //commentThreads.items[row].snippet.topLevelComment.snippet.authorDisplayName,                
                commentThreads.items[row].snippet.topLevelComment.snippet.textDisplay,
                commentThreads.items[row].snippet.topLevelComment.snippet.publishedAt,
              //  commentThreads.items[row].snippet.topLevelComment.snippet.likeCount,
                //commentThreads.items[row].snippet.totalReplyCount,'','','',''
            ]);
        if(commentThreads.items[row].snippet.totalReplyCount>0){
          parent = commentThreads.items[row].snippet.topLevelComment.id
          var nextPageTokenRep = undefined
          while(true){
            var commentThreads2 = YouTube.Comments.list('snippet', {videoId: vid, maxResults: 100, pageToken: nextPageTokenRep,parentId:parent})
            nextPageTokenRep=commentThreads2.nextPageToken;
            for (var i = commentThreads2.items.length-1;i>=0;i--){
              result.push(['', '','','','','',
                      commentThreads2.items[i].snippet.authorDisplayName,
                      commentThreads2.items[i].snippet.textDisplay,
                      commentThreads2.items[i].snippet.publishedAt,
                      commentThreads2.items[i].snippet.updatedAt]);
            }
            if(nextPageTokenRep == "" || typeof nextPageTokenRep === "undefined"){
              break
            }
          } 
        }
      }   
    if(nextPageToken =="" || typeof nextPageToken === "undefined"){
      break;
    }
  }

  var newSheet = sheet.insertSheet(sheet.getNumSheets());
  newSheet.getRange(1, 1,result.length,10).setValues(result);
}