function max(num1, num2)

   if (num1 > num2) then
      result = num1;
   else
      result = num2;
   end

   return result; 
end

shortmem = nil

function short_mem(mem0, mem1)
	result = nil
	if (mem0 ~= shortmem) then
		if (mem0 ~= nil) then
			result = mem0;
		else if (mem1 ~= nil) then
			result = mem1;
		end
	end
	else if (mem1 ~= shortmem) then
		if (mem1 ~= nil) then
			result = mem1;
		end
		else if (mem0 ~= nil) then
			result = mem0;
		end
	end
end
	shortmem = result;
	return result;
end
--[[ print(short_mem(1,2))
print(short_mem(1,2))
print(short_mem(1,2))
]]
function remem(memo)
	math.randomseed(os.time())
	random = math.random(0,1)
	if (random >= 0.5) then
		result = short_mem(memo,nil)
	else
		result = short_mem(nil,memo)
	end
	return result;
end

-- print(max(2,1))
-- this is not the end. just tell me what happened? what do you need to process?
