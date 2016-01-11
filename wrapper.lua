function on_msg_receive (msg)

  if started == 0 then
    return
  end
  if msg.out then
    return
  end

  --------------------------------------------
  if msg.text then
    mark_read (msg.from.print_name, ok_cb, false)

  end
  --------------------------------------------
  if (msg.from.print_name == 'Hasi') then
    os.execute (string.format("python3 listener.py \"%s\" &", msg.text))
  end
  --------------------------------------------

end
